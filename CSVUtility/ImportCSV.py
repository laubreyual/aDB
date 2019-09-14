import csv, ast, os
from pathlib import Path

# GLOBAL VARIABLE
table_list = {}

# TABLE VARS
table_name = ""
table_cols_def = []
table_cols = set()

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

	csv_table = csv_table_name[0].lower()
	table_name = csv_table
	
	if csv_table in table_list:
		table_cols_def = ast.literal_eval(table_list[csv_table])
	
		for cols in table_cols_def:
			table_cols.add(cols)
		
		if set(map(str.lower,table_cols)) == set(map(str.lower,csv_table_cols)):
			for row in csvReader:
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