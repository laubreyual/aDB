import csv, ast, os
from pathlib import Path
from cerberus import Validator
v = Validator()

# GLOBAL VARIABLE
table_list = {}

# TABLE VARS
table_name = ""
table_cols_def = []
table_cols = []

# CSV VARS
csv_table_name = ""
csv_table_cols = []
csv_row_data = []

with open('table_struc.txt') as f: # STATIC FOR NOW 
	for line in f:
		(key, val) = line.split("=")
		table_list[key.strip()] = val.strip() # STORE LIST OF TABLE STRUCTURES FROM FILE

with open('sample_table1.csv') as csvDataFile: # STATIC FOR NOW 
	csvReader = csv.reader(csvDataFile)
	csv_table_name = next(csvReader, None) # GET TABLE NAME FROM CSV
	csv_table_cols = next(csvReader, 1) # GET TABLE COLS DEFINITION FROM CSV
	csv_table_cols = [item.lower() for item in csv_table_cols]
	csv_table = csv_table_name[0].lower()
	table_name = csv_table
	
	if csv_table in table_list:
		table_cols_def = ast.literal_eval(table_list[csv_table])
		
		# ==============================================
		# START : DATA VALIDATION
		# ==============================================

		# TEST DATA
		# document = { 
		#   "id": "sample",
		#   "fname": "Juan",
		# 	"bday":"2019/10/01"
		# }
		schema = table_cols_def

		for key,value in schema.items():
			for key1,val in value.items():				
				schema[key][key1]=val.replace("int","integer").replace("varchar","string")
		
		# v.validate(document, schema)  # RETURNS TRUE/FALSE
		# print(v.errors) # PRINTS THE ERROR MESSAGE

		# ==============================================
		# END : DATA VALIDATION
		# ==============================================
		
		for cols in table_cols_def:		
			table_cols.append(cols)
		
		if set(table_cols) == set(csv_table_cols):
			for row in csvReader:
				is_valid_data = True
				csv_validate_data = {}
				for col in table_cols:
					csv_validate_data[col] = int(row[csv_table_cols.index(col)]) if row[csv_table_cols.index(col)].isdigit() else row[csv_table_cols.index(col)]
			
				is_valid_data = v.validate(csv_validate_data, schema)  # RETURNS TRUE/FALSE
				print(v.errors) # PRINTS THE ERROR MESSAGE
				if is_valid_data:
					csv_row_data.append(row)

					file_name = table_name+".txt"
					file_path = Path(file_name)
					file_path.touch(exist_ok=True)
					file = open(file_path)

					with open(file_name, mode='a+') as write_csv_file:
						writer = csv.writer(write_csv_file, None)

						for value in csv_row_data:
							writer.writerow(value) # STORE CSV DATA TO TEXT FILE				
		else:
			print("Invalid Column Headers")
	
	else:
		print("Table not found.")