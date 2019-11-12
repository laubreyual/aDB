import csv, ast, os, sys, random
from pathlib import Path

IMPORT_FILE_LOC = "import_files/"

class GenerateRecord:

	def main(self, table, column, primary_key, count):
		max_record = count
		row_count = 1
		col_count = 0
		col_name = column
		table_name = [table]				

		file_name = IMPORT_FILE_LOC+table_name[0]+".csv"
		file_path = Path(file_name)		
		file_path.touch(exist_ok=True)
		file = open(file_path)

		with open(file_name, mode='a+', newline='') as write_csv_file:
			writer = csv.writer(write_csv_file, delimiter=',', lineterminator='\r\n', quotechar = "'")
			writer.writerow(table_name)
			writer.writerow(col_name)

			while row_count <= max_record:
				row = []				
				# while col_count < len(col_name):
				for key, val in col_name.items():						
					if val == 'varchar':						
						row.append('"'+key+str(row_count)+'"')
					elif val == 'float':
						row.append(str(random.randint(1,500)))
					elif val == 'date':
						row.append(str(str(random.randint(1700,2019)))+"-"+str(str(random.randint(1,12)))+"-"+str(str(random.randint(1,31))))											

				row_count += 1							
				writer.writerow(row) # STORE CSV DATA TO TEXT FILE
