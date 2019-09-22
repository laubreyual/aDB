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

