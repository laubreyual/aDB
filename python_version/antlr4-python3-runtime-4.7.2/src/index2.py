import sys
from antlr4 import *
from MySQLLexer import MySQLLexer
from MySQLParser import MySQLParser
from MySQLListener import MySQLListener
from BTrees.OOBTree import OOBTree
from DatabasePY import *
from antlr4.error.ErrorListener import ErrorListener
from tabulate import tabulate
from SQLError import *
import copy
import datetime
import os

row_count = 0

class SQLErrorListener(ErrorListener):
	def __init__(self):
		super(SQLErrorListener, self).__init__()
	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		raise SQLError("Syntax error")

class InterpreterListener(MySQLListener):
	command = None
	columns = []
	tables = []
	conditions = []
	logicals = []
	attributes = {}
	insert_values = []
	insert_dtypes = []

	def enterS(self, ctx:MySQLParser.SContext):
		InterpreterListener.command = "select"
	def enterDelete_c(self, ctx:MySQLParser.Delete_cContext):
		InterpreterListener.command = "delete"
	def enterInsert_c(self, ctx:MySQLParser.Insert_cContext):
		InterpreterListener.command = "insert"
	def enterCreate_c(self, ctx:MySQLParser.Create_cContext):
		InterpreterListener.command = "create"
	def enterDescribe_c(self, ctx:MySQLParser.Describe_cContext):
		InterpreterListener.command = "describe"
		InterpreterListener.tables.append(str(ctx.IDENTIFIER()))
	def enterExit_c(self, ctx:MySQLParser.Exit_cContext):
		InterpreterListener.command = "exit"
	def enterShow_c(self, ctx:MySQLParser.Show_cContext):
		InterpreterListener.command = "show"
	def enterDrop_c(self, ctx:MySQLParser.Drop_cContext):
		InterpreterListener.command = "drop"
	def exitColumn_name(self, ctx:MySQLParser.Column_nameContext):
		name = ctx.IDENTIFIER()
		dot_name = ctx.DOT_IDENTIFIER()
		if dot_name != None:
			name = str(name) + str(dot_name)
		InterpreterListener.columns.append(str(name))

	def exitTable(self, ctx:MySQLParser.TableContext):
		i = 0
		while True:
			name = ctx.IDENTIFIER(i)
			i+=1
			if name == None:
				break
			InterpreterListener.tables.append(str(name))
	def exitS_condition(self, ctx:MySQLParser.S_conditionContext):
		variable = ctx.IDENTIFIER(0)
		dot_name = ctx.DOT_IDENTIFIER()
		op = ctx.RELATIONAL()
		if dot_name != None:
			variable = str(variable) + str(dot_name)

		if ctx.IDENTIFIER(1) != None:
			value = str(ctx.IDENTIFIER(1))
			data_type = "two_var"
		elif ctx.NUMBER() != None:
			value = float(str(ctx.NUMBER()))
			data_type = "float"
		elif ctx.STRING() != None:
			value = str(ctx.STRING())[1:-1]
			data_type = "varchar"
		else:
			value = str(ctx.DATE())[1:-1]
			data_type = "date"
		InterpreterListener.conditions.append([str(variable), str(op), value, data_type])
	def exitLogical(self, ctx:MySQLParser.LogicalContext):
		if ctx.AND() != None:
			InterpreterListener.logicals.append("AND")
		elif ctx.OR() != None:
			InterpreterListener.logicals.append("OR")
	def exitAttributes(self, ctx:MySQLParser.AttributesContext):
		i = 0		
		while True:
			(key, value) = str(ctx.ATTRIBUTE(i)).split(" ")	
			i+=1
			InterpreterListener.attributes[key] = value
			if ctx.ATTRIBUTE(i) == None:
				break
	def exitValues_c(self, ctx:MySQLParser.Values_cContext):
		for i in range(len(ctx.value())):
			if ctx.value(i).NUMBER():
				val = float(str(ctx.value(i).NUMBER()))
				data_type = 'float'
			elif ctx.value(i).DATE():
				val = str(ctx.value(i).DATE())[1:-1]
				data_type = 'date'
			else:
				val = str(ctx.value(i).STRING())[1:-1]
				data_type = 'varchar'
			InterpreterListener.insert_values.append(val)
			InterpreterListener.insert_dtypes.append(data_type)
	def resetVariables():
		InterpreterListener.command = None
		InterpreterListener.columns = []
		InterpreterListener.tables = []
		InterpreterListener.conditions = []
		InterpreterListener.logicals = []
		InterpreterListener.insert_values = []
		InterpreterListener.insert_dtypes = []
		InterpreterListener.attributes = {}

def evaluateCondition(op1, op2, operator):
	
	if operator == "=":
		return op1 == op2
	elif operator == ">":
		return op1 > op2
	elif operator == ">=":
		return op1 >= op2
	elif operator == "<":
		return op1 < op2
	elif operator == "<=":
		return op1 <= op2
	elif operator == "!=":
		return op1 != op2
	else:
		return False

def pushCondition(database, table_schema, tables, conditions):
	newDatabase = {}
	for table in tables:
		temp = database[table]
		inCondition = False
		for c in conditions:
			 if c[0] == table:
			 	condition = c
			 	inCondition = True
			 	break
		if inCondition and len(condition)<6: #not two var
			newTree = OOBTree()
			for key in temp:
				if condition[1] == 0: #key column
					value = key
				else:
					value = temp[key][condition[1]-1]
				if evaluateCondition(value, condition[3], condition[2]):
					newTree.update({key:temp[key]})
			newDatabase[table] = newTree

		else:
			newDatabase[table] = temp

	return database

def printDataRecursive(database, headers, tabulated, l, table_column, conditions, logicals, isPrintAll, isIncluded):
	#print("Table column", table_column)
	if len(table_column)>0:
		table = table_column[0]
		key_index = -1
		for key in database[table[0]]:
			key_index += 1
			if isPrintAll:
				to_print = [key] + database[table[0]][key]
			elif 0 in table[1]: #key is included
				to_print = [key]+[database[table[0]][key][index-1] for index in table[1][1:]]
			else:
				to_print = [database[table[0]][key][index-1] for index in table[1]]
			
			isIncluded_new = isIncluded
			conditions = copy.deepcopy(conditions)
			for condition in conditions:
				if len(condition)>5 and condition[5] == "two_var":
					if condition[0] == table[0]:
						#get the value of the attribute
						if condition[1] == 0: #key attribute
							condition[6] = key
						else:
							condition[6] = database[table[0]][key][condition[1]-1]
					if condition[3] == table[0]:
						#get the value of the attribute
						if condition[4] == 0: #key attribute
							condition[7] = key
						else:
							condition[7] = database[table[0]][key][condition[4]-1]
					if condition[6] != None and condition[7] != None:
						if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
							isIncluded_new = isIncluded_new and evaluateCondition(condition[6], condition[7], condition[2])
						elif logicals[0] == 'OR':
							isIncluded_new = isIncluded_new or evaluateCondition(condition[6], condition[7], condition[2])
						# if key_index == len(database[table[0]])-1:
						# 	condition[6] = condition[7] = None
				elif condition[0] == table[0]:
					if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
						if condition[1] == 0: #primary key column
							isIncluded_new = isIncluded_new and evaluateCondition(key, condition[3], condition[2])
						else:
							isIncluded_new = isIncluded_new and evaluateCondition(database[table[0]][key][condition[1]-1], condition[3], condition[2])
					elif logicals[0] == 'OR':
						if condition[1] == 0: #primary key column
							isIncluded_new = isIncluded_new or evaluateCondition(key, condition[3], condition[2])
						else:
							isIncluded_new = isIncluded_new or evaluateCondition(database[table[0]][key][condition[1]-1], condition[3], condition[2])
			

			printDataRecursive(database, headers, tabulated, l+to_print, table_column[1:], conditions[:], logicals, isPrintAll, isIncluded_new)
	elif isIncluded:
		tabulated.append(l)
		global row_count
		row_count += 1


def printData(database, table_schema):
	tables = InterpreterListener.tables
	columns = InterpreterListener.columns
	conditions = InterpreterListener.conditions
	logicals = InterpreterListener.logicals

	#get the column header
	if len(columns) > 0:
		column_headers = columns
	else: # the column specified was *
		temp = []
		for table in tables:
			temp += table_schema[table][0]
		column_headers = temp


	#get the index of the columns to be printed and its table name
	table_column = []
	for table in tables:
		list_columns = []
		for column in columns:
			column = column.split(".")
			if column[0] == table:
				index = table_schema[table][0].index(column[1])
				list_columns.append(index)
		table_column.append([table, list_columns])

	#fix the condition
	for index in range(0, len(conditions)):
		temp = conditions[index][0].split(".")
		table_name = temp[0]
		column_index = table_schema[table_name][0].index((temp[1]))
		conditions[index] = [table_name, column_index]+ conditions[index][1:]
		if conditions[index][4] == "two_var":
			temp = conditions[index][3].split(".")
			table_name = temp[0]
			column_index = table_schema[table_name][0].index((temp[1]))
			conditions[index] = conditions[index][:3] + [table_name, column_index] + conditions[index][4:]
	
	#assuming two conditions only with one logical
	if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
		isIncluded = True
		database = pushCondition(database, table_schema, tables, conditions)
	else:
		isIncluded = False

	tabulated = []
	printDataRecursive(database, column_headers, tabulated, [], table_column, conditions, logicals, not len(columns)>0, isIncluded)
	if len(tabulated)>0:
		print(tabulate(tabulated, headers=column_headers, tablefmt='orgtbl'))
		global row_count
		print("Row Count:", len(tabulated))
	else:
		print("Row Count: 0")
		
def createTable(database, list_tables):
	toPrint = []
	header = []
	tables = InterpreterListener.tables
	attributes = InterpreterListener.attributes
	table_name = str(tables[0])
	table_schema = table_name+";"
	i = 0	
	for key, datatype in attributes.items():
		dtype = datatype.replace("(",";").replace(")",";")
		if dtype == "date":
			dtype += ";None;"

		elif dtype.startswith('varchar'):
			length = int(dtype.split(';')[1])
			if length < 0 or length > 300:
				raise StringSizeError()

		elif dtype.startswith('float'):
			restrictions = dtype.split(';')[1].split(',')
			digits = int(restrictions[0])
			precisions = int(restrictions[1])

			if precisions > digits:
				raise FloatSizeError('larger')
			if digits < 1 or digits > 9:
				raise FloatSizeError('digits')
			if precisions < 0 or precisions > 4:
				raise FloatSizeError('precisions')

		table_schema += str(key)+";"+str(dtype)
		
	table_schema = table_schema[:-1]	
	saveTableToSchema(table_schema, table_name)

	header.append("COMMAND EXECUTED SUCCESSFULLY")
	toPrint.append(["CREATED TABLE "+table_name])
	print(tabulate(toPrint, headers=header, tablefmt='orgtbl'))

def checkTables(db_tables):
	for table in InterpreterListener.tables:
		if table not in db_tables:
			raise TableNotFoundError(table)

def checkExistingTable(db_tables):
	for table in InterpreterListener.tables:
		if table in db_tables:
			raise TableFoundError(table)

# def checkDataType(datatypes, list_vartype):
# 	for key, value in datatypes:
# 			datatype = (value.split("(")[0])			
# 			if datatype.lower() not in list_vartype:
# 				raise DataTypeNotFound(datatype)

def checkColumns(table_schema):
	for index in range(0, len(InterpreterListener.columns)):
		column = InterpreterListener.columns[index]
		column_found = False
		if "." not in column:
			for table in InterpreterListener.tables:
				if column in table_schema[table][0]:
					column_found = True
					InterpreterListener.columns[index] = table + "." + column
					break
		else:
			column_name = column.split(".")[1]
			table = column.split(".")[0]
			if column_name in table_schema[table][0]:
				column_found = True

		if not column_found:
			raise ColumnNotFoundError(column, table)

def checkConditions(table_schema):
		for index in range(0, len(InterpreterListener.conditions)):
			j = InterpreterListener.conditions[index]
			# j[0] = condition variable
			column_found = False
			if "." not in j[0] and j[3] != "two_var":
				for i in InterpreterListener.tables:
					if j[0] in table_schema[i][0]:
						column_found = True
						#check data type

						data_type = table_schema[i][1][table_schema[i][0].index(j[0])][0]
						if j[3] != data_type:
							if j[3] == "date" and data_type == "varchar":
								InterpreterListener.conditions[index][3] = "varchar"
							else:
								raise DataTypeNotMatchError(j[0], data_type, j[2])
						InterpreterListener.conditions[index][0] = i + "." + j[0]
						break
			elif j[3] != "two_var":
				column_name = j[0][j[0].find(".")+1:]
				table_name = j[0][0:j[0].find(".")]

				if column_name in table_schema[table_name][0]:
					column_found = True
				data_type = table_schema[table_name][1][table_schema[table_name][0].index(column_name)][0]
				if data_type != j[3]:
					if j[3] == "date" and data_type == "varchar":
						InterpreterListener.conditions[index][3] = "varchar"
					else:
						raise DataTypeNotMatchError(j[0], data_type, j[2])

			#case of two variables in the same condition
			else:
				for i in InterpreterListener.tables:
					#for the first variable
					if j[0] in table_schema[i][0] and "." not in j[0]:
						InterpreterListener.conditions[index][0] = i + "." + j[0]
					#for the second variable
					if j[2] in table_schema[i][0] and "." not in j[2]:
						InterpreterListener.conditions[index][2] = i + "." + j[2]
					if "." in j[0] and "." in j[2]:
						if j[0][j[0].find(".")+1:] in table_schema[j[0][0:j[0].find(".")]][0] and j[2][j[2].find(".")+1:] in table_schema[j[2][0:j[2].find(".")]][0]:
							column_found = True
						break
				if column_found:
					j.append(None)
					j.append(None)
					tb_name1 = j[0][:j[0].find(".")]
					tb_name2 = j[2][:j[2].find(".")]
					col_name1 = j[0][j[0].find(".")+1:]
					col_name2 = j[2][j[2].find(".")+1:]
					col_index_1 = table_schema[tb_name1][0].index(col_name1)
					col_index_2 = table_schema[tb_name2][0].index(col_name2)
					if table_schema[tb_name1][1][col_index_1][0] != table_schema[tb_name2][1][col_index_2][0]:
						raise DataTypeNotMatchError(col_name1, table_schema[tb_name1][1][col_index_1], col_name2, table_schema[tb_name2][1][col_index_2])

			if not column_found:
				raise ColumnNotFoundError('too many', 'too many')

def checkValidVarchar(varchar, column_name, length):
	if len(varchar) > length:
		raise InvalidStringLengthError(varchar, column_name, length)
	
	return varchar

def checkValidFloat(number, column_name, restriction):
	# TODO: check valid float, number of digits, precisions
	if number > 65000 or number < -65000:
		raise InvalidFloatError(number, restriction, 'limit')

	return number

def checkValidDate(date):
	# quotes = date[0]
	try:
		datetime.datetime.strptime(date, '%Y-%m-%d')
	except ValueError as e:
		print('>', e)
		raise InvalidDateError(date)

	return date

def checkDeleteData(table_schema, database):
	table_count = len(InterpreterListener.tables)
	if table_count > 1:
		raise SQLException('Too many tables for DELETE')
	# print("Command:", InterpreterListener.command)
	# print("Columns:", InterpreterListener.columns)
	# print("Tables:", InterpreterListener.tables)
	# print("Conditions:", InterpreterListener.conditions)
	# print("Logicals:", InterpreterListener.logicals)
	# print("Attributes:", InterpreterListener.attributes)

	# Checking for foreign key constraint here

def deleteFromTable(database, table_schema):
	table_name = InterpreterListener.tables[0]
	conditions = InterpreterListener.conditions
	logicals = InterpreterListener.logicals

	if len(logicals) == 0:
		logicals.append('AND')

	table = database[table_name]

	for index in range(0, len(conditions)):
		temp = conditions[index][0].split(".")
		table_name = temp[0]
		column_index = table_schema[table_name][0].index((temp[1]))
		conditions[index] = [table_name, column_index]+ conditions[index][1:]
	
	print(conditions)
	for key in list(table.keys()):
		if logicals[0] == 'AND':
			toDelete = True
		else:
			toDelete = False

		for c in conditions:
			op2 = c[3]
			if c[1] == 0:
				op1 = key
			else:
				op1 = table[key][c[1]-1]

			if logicals[0] == 'AND':
				toDelete = toDelete and evaluateCondition(op1, op2, c[2])
			else:
				toDelete = toDelete or evaluateCondition(op1, op2, c[2])

		if toDelete:
			table.pop(key)



def checkInsertData(table_schema, database):
	table_count = len(InterpreterListener.tables)
	if table_count > 1:
		raise SQLException('Too many tables for INSERT')

	table_name = InterpreterListener.tables[0]
	column_count = len(InterpreterListener.columns)

	query_values = InterpreterListener.insert_values # values from query
	query_dtypes = InterpreterListener.insert_dtypes # data types derived from query_values; see exitValues_c()
	db_columns = table_schema[table_name][0]	# column names derived from table schema

	# the first if-else blocks are for checking the data type and string length
	if column_count == 0:
		# if there is no columns stated, values() should follow the same order in table_schema
		db_dtypes = [i for i in table_schema[table_name][1]]
		query_columns = db_columns
		primary_key = query_values[0]

		for i in range(len(query_dtypes)):
			if db_dtypes[i][0] != query_dtypes[i]:
				raise DataTypeNotMatchError(query_values[i], query_dtypes[i], db_columns[i], db_dtypes[i][0])

			if db_dtypes[i][0] == 'varchar':
				query_values[i] = checkValidVarchar(query_values[i], db_columns[i], db_dtypes[i][1])
			elif db_dtypes[i][0] == 'date':
				query_values[i] = checkValidDate(query_values[i])
			elif db_dtypes[i][0] == 'float':
				query_values[i] = checkValidFloat(query_values[i], db_columns[i], db_dtypes[i][1])

	else:
		query_columns = [column.split('.')[1] for column in InterpreterListener.columns]
		db_dtypes = []
		db_columns_lookup = dict()
		primary_attrib = db_columns[0]


		if primary_attrib not in db_columns:
			raise SQLError('Primary key/attribute "{}" should be included when inserting.'.format(primary_attrib))

		for i in range(len(db_columns)):
			db_columns_lookup[db_columns[i]] = table_schema[table_name][1][i]

		for i in range(len(query_columns)):
			# the data type will be checked depending on the order of columns stated in the query
			db_dtype = db_columns_lookup[ query_columns[i] ]

			if query_columns[i] == primary_attrib:
				primary_key = query_values[i]

			if db_dtype[0] != query_dtypes[i]:
				raise DataTypeNotMatchError(query_values[i], query_dtypes[i], query_columns[i], db_dtype[0])

			if db_dtype[0] == 'varchar':
				query_values[i] = checkValidVarchar(query_values[i], query_columns[i], db_dtype[1])
			elif db_dtype[0] == 'date':
				query_values[i] = checkValidDate(query_values[i])
			elif db_dtype[0] == 'float':
				query_values[i] = checkValidFloat(query_values[i], query_columns[i], db_dtype[1])
	
	table = database[table_name]

	if primary_key in table.keys():
		# checking for primary key; TODO: check foreign key
		raise PrimaryKeyAlreadyExistsError(primary_key, table_name)

	# swap the position of values to mirror schema; for easier insertion
	for i in range(len(db_columns)):
		for j in range(len(db_columns)):
			if db_columns[i] == query_columns[j]:
				query_columns[i], query_columns[j] = query_columns[j], query_columns[i]
				query_values[i], query_values[j] = query_values[j], query_values[i]

	return table_name, query_values

def describeTable(table, table_schema):
	header = ["Field", "Type", "Key"]
	columns = table_schema[table][0]
	types = table_schema[table][1]
	toPrint = []

	for i in range(0, len(columns)):
		key = ''
		if i == 0:
			key = 'PRI'
		if types[i][0] != "date":
			data_type = '{}({})'.format(types[i][0], str(types[i][1]).replace('(','').replace(')',''))
		else:
			data_type = types[i][0]
		toPrint.append([columns[i], data_type, key])
	print(tabulate(toPrint, headers=header, tablefmt='orgtbl'))

def showTables(list_tables):
	tabulated = []
	for table in list_tables:
		tabulated.append([table])
	print(tabulate(tabulated, headers=["Tables"], tablefmt='orgtbl'))

def dropTables(list_tables, table_schema, database):
	tables_to_delete = InterpreterListener.tables
	checkTables(list_tables)
	for table_name in tables_to_delete:
		if table_name in list_tables:
			list_tables.remove(table_name)
		if table_name in table_schema:
			table_schema.pop(table_name)
		if table_name in database:
			database.pop(table_name)
		if os.path.isfile("database_files/"+table_name+".csv"):
			os.remove("database_files/"+table_name+".csv")
	saveDatabase(database, list_tables, table_schema)
	print("Query OK")


def insertDataIntoTable(db_table, query_values):
	db_table.update( {query_values[0] : query_values[1:]} )
	print('> Insert succesful.');


def main(argv):
	database = {}
	list_tables = []
	table_schema = {}
	list_vartype = ["float", "varchar", "date"]
	#list_tables = ["sample", "sample2", "person"]
	#index 0 is always the primary key
	# table_schema = {"sample":[["a", "b", "c"],[("number", None), ("string", 50), ("string", 50)]],
	# 				"sample2":[["d", "e", "f"],[("number", None), ("string", 50), ("string", 50)]],
	# 				"person":[["id", "name", "birthdate"],[("number", None), ("string", 50), ("date", None)]]}

	loadTables(list_tables, table_schema)
	# print(list_tables)
	# print(table_schema)

	for table in list_tables:
		loadDatabase(database, table)
	while True:
		# input_stream = FileStream(argv[1])
		input_stream = InputStream(input("mysql> "))

		try:

			lexer = MySQLLexer(input_stream)

			stream = CommonTokenStream(lexer)

			parser = MySQLParser(stream)

			parser.addErrorListener(SQLErrorListener())

			tree = parser.s()

			interpreter = InterpreterListener()

			walker = ParseTreeWalker()

			walker.walk(interpreter, tree)

			


			try:

				if interpreter.command=="exit":

					break

				elif interpreter.command=="select":

					checkTables(list_tables)

					checkColumns(table_schema)

					checkConditions(table_schema)

					printData(database, table_schema)


				elif interpreter.command=="describe":

					checkTables(list_tables)

					describeTable(InterpreterListener.tables[0], table_schema)


				elif interpreter.command=='insert':
					checkTables(list_tables)
					checkColumns(table_schema)
					table_name, query_values = checkInsertData(table_schema, database)
					insertDataIntoTable(database[table_name], query_values)

				elif interpreter.command=="create":
					checkExistingTable(list_tables)
					# checkDataType(InterpreterListener.attributes.items(), list_vartype)
					createTable(database, list_tables)
					loadTables(list_tables, table_schema)
					for table in list_tables:
						loadDatabase(database, table)

				elif interpreter.command=="show":
					showTables(list_tables)

				elif interpreter.command=="drop":
					dropTables(list_tables, table_schema, database)

				elif interpreter.command=="delete":
					checkTables(list_tables)
					checkColumns(table_schema)
					checkConditions(table_schema)
					checkDeleteData(table_schema, database)
					deleteFromTable(database, table_schema)
				
			except SQLError as e:
				print(e.message)
				print()

			finally:
				# print("Command:", InterpreterListener.command)

				# print("Columns:", InterpreterListener.columns)

				# print("Tables:", InterpreterListener.tables)

				# print("Conditions:", InterpreterListener.conditions)

				# print("Logicals:", InterpreterListener.logicals)

				# print("Attributes:", InterpreterListener.attributes)
				InterpreterListener.resetVariables()

				print()
		except Exception as e:
			print(e)

			print()
	# save database here
	saveDatabase(database, list_tables, table_schema)


if __name__ == '__main__':
	main(sys.argv)