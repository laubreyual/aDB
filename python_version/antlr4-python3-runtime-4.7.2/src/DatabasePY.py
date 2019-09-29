from BTrees.OOBTree import OOBTree

def loadDatabase(database, table):
	#load the data into a btree (assuming that the first column is the primary key)
	file = open("database_files/"+table+".csv", "r")
	t = OOBTree()
	for line in file:
		data = line[:-1].split(',')
		fixed_data = []
		i = 0
		while i<len(data):
			if data[i][0]!='"' and data[i][0]!="'":
				fixed_data.append(float(data[i]))
			elif (data[i][0]=="'" or data[i][0]=='"') and (data[i][-1]=="'" or data[i][-1]=='"'):
				fixed_data.append(data[i][1:-1])
			else:
				j=i+1
				temp = data[i][1:]
				while j<len(data):
					temp += ","+data[j]
					if data[j][-1]=="'" or data[j][-1]=='"':
						fixed_data.append(temp[:-1])
						break
					j+=1
				i=j
			i += 1
		t.update({fixed_data[0]:fixed_data[1:]})
	database[table] = t
	file.close()

def loadTables(list_tables, table_schema):
	file = open("database_files/table_schema", "r")

	for line in file:
		data = line[:-1].split(";")
		list_tables.append(data[0])
		columns = []
		data_types =[]
		i = 1
		while i < len(data):
			columns.append(data[i])
			if data[i+1] == "float":
				restrictions = data[i+2].split(",")
				data_types.append( (data[i+1], (int(restrictions[0]), int(restrictions[1]))) )
			elif data[i+1] == "varchar":
				data_types.append( (data[i+1], int(data[i+2])) )
			else:
				data_types.append( (data[i+1], None) )
			i+=3
		table_schema[data[0]] = [columns, data_types]
	file.close()

def saveDatabase(database, list_tables, table_schema):
	file = open("database_files/table_schema", "w")

	for table_name in table_schema:
		columns = table_schema[table_name][0]
		data_types = table_schema[table_name][1]
		to_write = table_name
		for index in range(0, len(columns)):
			dtype = str(data_types[index][0])
			restriction = data_types[index][1]
			if dtype == 'float':
				restriction = str(restriction).replace('(','').replace(')','').replace(' ','')

			to_write += str(";" + columns[index]) + ";" + str(dtype) + ";" + str(restriction)
		file.write(to_write+"\n")
	file.close()

	for table_name in list_tables:
		file = open("database_files/"+table_name+".csv", "w")
		data = database[table_name]
		for key in data:
			to_write = str(key)
			values = data[key]
			for value in values:
				if isinstance(value, str):
					to_write += ',"' + value + '"'
				else:
					to_write += "," + str(value)
			file.write(to_write+"\n")
		file.close()

def saveTableToSchema(table_schema, new_table):
	file = open("database_files/table_schema", "a")
	file.write(table_schema+"\n")
	file.close()

	file = open("database_files/"+new_table+".csv","w")


