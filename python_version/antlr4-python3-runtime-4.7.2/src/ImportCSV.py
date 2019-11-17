import csv, ast, os, sys
import datetime
from pathlib import Path
from SQLError import *

# GLOBAL VARIABLE
IMPORT_FILE_LOC = "import_files/"
DB_FILE_LOC = "database_files/"

checkValidationMsg = {}

def checkValidVarchar(varchar, column_name, length):
		checkValidationMsg = {}	
		try:		
			if len(varchar) > length:
				try:
					raise InvalidStringLengthError(varchar, column_name, length)
				except SQLError as e:
					checkValidationMsg[False] = e.message
					return checkValidationMsg
			checkValidationMsg[True] = ""
			return checkValidationMsg
		except: 
			checkValidationMsg[False] = "Data type did not match. "+column_name+" is of TYPE VARCHAR"
			return checkValidationMsg

def checkValidFloat(number, column_name, restriction):
	checkValidationMsg = {}	
	# TODO: check valid float, number of digits, precisions
	if not isinstance(number, int):
		checkValidationMsg[False] = "Invalid value for float "+number		
		return checkValidationMsg
	else:
		if number > 63000 or number < -63000:
			try:				
				raise InvalidFloatError(number, restriction, 'limit')
			except SQLError as e:
				checkValidationMsg[False] = e.message
				return checkValidationMsg	
		checkValidationMsg[True] = ""
		return checkValidationMsg

def checkValidDate(date):
	checkValidationMsg = {}		
	try:		
		datetime.datetime.strptime(date, '%Y-%m-%d')
	except ValueError as e:		
		checkValidationMsg[False] = e
		return checkValidationMsg	
	checkValidationMsg[True] = ""
	return checkValidationMsg
	
class CSVImport:	

	def main(self, filename):
		self.returnMsg = {}		

		# TABLE VARS
		self.table_list = {}
		self.table_name = ""
		self.table_cols_def = ""
		self.table_cols = []
		self.table_col_list = {}

		# CSV VARS
		self.csv_table_name = ""
		self.csv_table_cols = []
		self.csv_row_data = []
		self.db_pk_list = []

		input_stream = filename
		if input_stream.find(".csv") < 0:
			self.returnMsg[False] = "INVALID FILE TYPE." 
			return self.returnMsg
		else:
			file = open(DB_FILE_LOC+"table_schema", "r")
			for line in file:
				self.table_name = line.split(";")[0]
				table_columns = line.replace(str(self.table_name)+";", "")	
				self.table_list[self.table_name] = table_columns

			try:
				with open(input_stream) as csvDataFile: # STATIC FOR NOW 
					csvReader = csv.reader(csvDataFile, delimiter=',', lineterminator='\r\n', quotechar = "'")
					self.csv_table_name = next(csvReader, None) # GET TABLE NAME FROM CSV
					self.csv_table_cols = next(csvReader, 1) # GET TABLE COLS DEFINITION FROM CSV
					self.csv_table_cols = [item.lower() for item in self.csv_table_cols]
					csv_table = self.csv_table_name[0].lower()
					self.table_name = csv_table	

					with open(DB_FILE_LOC+csv_table+".csv") as dbDataFile: 
						dbCsvReader = csv.reader(dbDataFile, delimiter=',', lineterminator='\r\n', quotechar = "'")
						for row in dbCsvReader:
							self.db_pk_list.append(row[0])	
					
					if csv_table in self.table_list:
						self.table_cols_def = self.table_list[csv_table]
								
						ctr = 0
						col_name = ""
						col_type = ""
						col_len = ""
						for cols in self.table_cols_def.split(";"):			
							if ctr == 0 or ctr == 3:
								col_name = cols
								self.table_cols.append(cols)				
								ctr = 0
							if ctr == 1:
								col_type = cols
							if ctr == 2:
								col_len = cols
							ctr += 1
							self.table_col_list[col_name] = [col_type, col_len]		
						
						if set(self.table_cols) == set(self.csv_table_cols):
							isValidImport = True	
							invalidDataTypeMsg = ""					
							for row in csvReader:							
								is_valid_data = []
								csv_validate_data = {}
								for col in self.table_cols:
									data = int(row[self.csv_table_cols.index(col)]) if row[self.csv_table_cols.index(col)].isdigit() else row[self.csv_table_cols.index(col)]	
									
									if col == self.table_cols[0]:
										if str(data) in self.db_pk_list:
											self.returnMsg[False] = "DUPLICATE IN PRIMARY KEY FOUND"
											return self.returnMsg
											break

									# ==============================================
									# START : DATA VALIDATION
									# ==============================================		
									try:
										if self.table_col_list[col][0] == 'varchar':
											checkVar = checkValidVarchar(data, col, int(self.table_col_list[col][1]))
											for key, val in checkVar.items():
												is_valid_data.append(key)
												if not key:
													invalidDataTypeMsg = val
													break
										elif self.table_col_list[col][0] == 'date':
											checkDate = checkValidDate(data)
											for key, val in checkDate.items():
												is_valid_data.append(key)
												if not key:
													invalidDataTypeMsg = val
													break
										elif self.table_col_list[col][0] == 'float':
											checkFloat = checkValidFloat(data, col, self.table_col_list[col][1])
											for key, val in checkFloat.items():
												is_valid_data.append(key)
												if not key:
													invalidDataTypeMsg = val
													break										
									except:
										isValidImport = False
										break
									# ==============================================
									# END : DATA VALIDATION
									# ==============================================
									
								if False not in is_valid_data:									
									self.csv_row_data.append(row)
								else:
									self.csv_row_data = {}
									break						
							if False not in is_valid_data:	
								file_name = DB_FILE_LOC + self.table_name + ".csv"			
								file_path = Path(file_name)		
								file_path.touch(exist_ok=True)
								file = open(file_path)

								with open(file_name, mode='a+', newline='') as write_csv_file:
									writer = csv.writer(write_csv_file, delimiter=',', lineterminator='\r\n', quotechar = "'")							
									for value in self.csv_row_data:
										writer.writerow(value) # STORE CSV DATA TO TEXT FILE

								self.returnMsg[True] = "RECORD/S IMPORTED SUCCESSFULLY."
								return self.returnMsg
							else:
								self.returnMsg[False] = invalidDataTypeMsg
								return self.returnMsg
						else:								
							self.returnMsg[False] = "Invalid Column Headers" 
							return self.returnMsg
					
					else:
						self.returnMsg[False] = "TABLE "+self.table_name+" DOES NOT EXIST." 
						return self.returnMsg
			except:
				self.returnMsg[False] = "PROBLEM ENCOUNTERED IN: "+input_stream
				return self.returnMsg