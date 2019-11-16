import csv, ast, os, sys, random
import datetime
from pathlib import Path

IMPORT_FILE_LOC = "import_files/"

class GenerateRecord:

	def main(self, table, column, primary_key, count):
		max_record = count
		row_count = 1
		col_count = 0
		col_name = column
		table_name = [table]	
		primary_col = {}	
		primary_col[primary_key] = col_name.pop(primary_key, None)
		primary_col.update(col_name)		

		file_name = IMPORT_FILE_LOC+table_name[0]+".csv"
		file_path = Path(file_name)		
		file_path.touch(exist_ok=True)
		file = open(file_path)
		try:
			with open(file_name, mode='w', newline='') as write_csv_file:
				writer = csv.writer(write_csv_file, delimiter=',', lineterminator='\r\n', quotechar = "'")
				writer.writerow(table_name)
				writer.writerow(primary_col)

				while row_count <= max_record:
					row = []					
					for key, val in primary_col.items():					
						if key == primary_key:
							if val == 'varchar':	
								row.append('"'+key+str(row_count)+'"')
							elif val == 'float':
								row.append(str(row_count))
							# elif val == 'date':
							# 	row.append(str(str(random.randint(1700,2019)))+"-"+str(str(random.randint(1,12)))+"-"+str(str(random.randint(1,31))))
						else:						
							if val == 'varchar':						
								row.append('"'+key+str(row_count)+'"')
							elif val == 'float':
								row.append(str(random.randint(1,50000)))
							elif val == 'date':								
								year = str(random.randint(1700,2019))
								month = str(random.randint(1,12))
								day = str(random.randint(1,31))
								gen_date = year+"-"+month+"-"+day							
								row.append(str(gen_date))	

					row_count += 1						
					writer.writerow(row) # STORE CSV DATA TO TEXT FILE
				file.close()
		except:
			pass
