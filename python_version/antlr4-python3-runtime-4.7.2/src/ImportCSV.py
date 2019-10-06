import csv, ast, os, sys
import datetime
from pathlib import Path
from SQLError import *

# GLOBAL VARIABLE
table_list = {}
IMPORT_FILE_LOC = "import_files/"
DB_FILE_LOC = "database_files/"

# TABLE VARS
table_name = ""
table_cols_def = ""
table_cols = []
table_col_list = {}

# CSV VARS
csv_table_name = ""
csv_table_cols = []
csv_row_data = []

def checkValidVarchar(varchar, column_name, length):
	if len(varchar) > length:
		raise InvalidStringLengthError(varchar, column_name, length)
		return False
	return True

def checkValidFloat(number, column_name, restriction):
	# TODO: check valid float, number of digits, precisions
	if not isinstance(number, int):
		print("Invalid value for float "+number)
		# raise InvalidFloatError(number, restriction, 'limit')
		return False
	else:
		if number > 65000 or number < -65000:
			raise InvalidFloatError(number, restriction, 'limit')
			return False
		return True

def checkValidDate(date):
	# quotes = date[0]
	try:
		datetime.datetime.strptime(date, '%Y-%m-%d')
	except ValueError as e:
		print('>', e)
		print("Invalid date.")
		# raise InvalidDateError(date)
		return False
	return True

file = open(DB_FILE_LOC+"table_schema", "r")
for line in file:
	table_name = line.split(";")[0]
	table_columns = line.replace(str(table_name)+";", "")	
	table_list[table_name] = table_columns

input_stream = input("enter filepath> ")
try:
	with open(input_stream) as csvDataFile: # STATIC FOR NOW 
		csvReader = csv.reader(csvDataFile)
		csv_table_name = next(csvReader, None) # GET TABLE NAME FROM CSV
		csv_table_cols = next(csvReader, 1) # GET TABLE COLS DEFINITION FROM CSV
		csv_table_cols = [item.lower() for item in csv_table_cols]
		csv_table = csv_table_name[0].lower()
		table_name = csv_table	
		
		if csv_table in table_list:
			table_cols_def = table_list[csv_table]
					
			ctr = 0
			col_name = ""
			col_type = ""
			col_len = ""
			for cols in table_cols_def.split(";"):			
				if ctr == 0 or ctr == 3:
					col_name = cols
					table_cols.append(cols)				
					ctr = 0
				if ctr == 1:
					col_type = cols
				if ctr == 2:
					col_len = cols
				ctr += 1
				table_col_list[col_name] = [col_type, col_len]		
			
			if set(table_cols) == set(csv_table_cols):
				for row in csvReader:
					is_valid_data = []
					csv_validate_data = {}
					for col in table_cols:
						data = int(row[csv_table_cols.index(col)]) if row[csv_table_cols.index(col)].isdigit() else row[csv_table_cols.index(col)]	
												
						# ==============================================
						# START : DATA VALIDATION
						# ==============================================		

						if table_col_list[col][0] == 'varchar':
							is_valid_data.append(checkValidVarchar(data, col, int(table_col_list[col][1])))
						elif table_col_list[col][0] == 'date':
							is_valid_data.append(checkValidDate(data))
						elif table_col_list[col][0] == 'float':						
							is_valid_data.append(checkValidFloat(data, col, table_col_list[col][1]))

						# ==============================================
						# END : DATA VALIDATION
						# ==============================================
						
					if False not in is_valid_data:									
						csv_row_data.append(row)
					else:
						csv_row_data = {}
						break
				
				file_name = DB_FILE_LOC+table_name+".csv"			
				file_path = Path(file_name)		
				file_path.touch(exist_ok=True)
				file = open(file_path)

				with open(file_name, mode='a+', newline='') as write_csv_file:
					writer = csv.writer(write_csv_file, None)
					for value in csv_row_data:
						writer.writerow(value) # STORE CSV DATA TO TEXT FILE							
			else:
				print("Invalid Column Headers")
		
		else:
			print("Table not found.")
except:
	print(input_stream+" file does not exists")