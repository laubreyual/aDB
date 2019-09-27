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

row_count = 0

class SQLErrorListener(ErrorListener):
	def __init__(self):
		super(SQLErrorListener, self).__init__()
	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		raise Exception("Syntax error")

class InterpreterListener(MySQLListener):
	command = None
	columns = []
	tables = []
	conditions = []
	logicals = []

	def enterS(self, ctx:MySQLParser.SContext):
		InterpreterListener.command = "select"
	def enterDelete_c(self, ctx:MySQLParser.Delete_cContext):
		InterpreterListener.command = "delete"
	def enterInsert_c(self, ctx:MySQLParser.Insert_cContext):
		InterpreterListener.command = "insert"
	def enterCreate_c(self, ctx:MySQLParser.Create_cContext):
		InterpreterListener.command = "create"
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
			data_type = "number"
		elif ctx.STRING() != None:
			value = str(ctx.STRING())[1:-1]
			data_type = "string"
		else:
			value = str(ctx.DATE())[1:-1]
			data_type = "date"
		InterpreterListener.conditions.append([str(variable), str(op), value, data_type])
	def exitLogical(self, ctx:MySQLParser.LogicalContext):
		if ctx.AND() != None:
			InterpreterListener.logicals.append("AND")
		elif ctx.OR() != None:
			InterpreterListener.logicals.append("OR")

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

def printDataRecursive(database, headers, tabulated, l, table_column, conditions, logicals, isPrintAll, isIncluded):
	#print("Table column", table_column)
	if len(table_column)>0:
		table = table_column[0]

		for key in database[table[0]]:
			if isPrintAll:
				to_print = [key] + database[table[0]][key]
			elif 0 in table[1]: #key is included
				to_print = [key]+[database[table[0]][key][index-1] for index in table[1][1:]]
			else:
				to_print = [database[table[0]][key][index-1] for index in table[1]]
			
			newCondition = False
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
							isIncluded_new = isIncluded and evaluateCondition(condition[6], condition[7], condition[2])
						elif logicals[0] == 'OR':
							isIncluded_new = isIncluded or evaluateCondition(condition[6], condition[7], condition[2])
						newCondition = True
				elif condition[0] == table[0]:
					if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
						if condition[1] == 0: #primary key column
							isIncluded_new = isIncluded and evaluateCondition(key, condition[3], condition[2])
						else:
							isIncluded_new = isIncluded and evaluateCondition(database[table[0]][key][condition[1]-1], condition[3], condition[2])
					elif logicals[0] == 'OR':
						if condition[1] == 0: #primary key column
							isIncluded_new = isIncluded or evaluateCondition(key, condition[3], condition[2])
						else:
							isIncluded_new = isIncluded or evaluateCondition(database[table[0]][key][condition[1]-1], condition[3], condition[2])
					newCondition = True
			if not newCondition:
				isIncluded_new = isIncluded
			printDataRecursive(database, headers, tabulated, l+to_print, table_column[1:], conditions, logicals, isPrintAll, isIncluded_new)
	elif isIncluded:
		tabulated.append(l)
		global row_count
		row_count += 1


def printData(database, table_schema):
	tables = InterpreterListener.tables
	columns = InterpreterListener.columns
	conditions = InterpreterListener.conditions
	logicals = InterpreterListener.logicals

	#print the column header
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

	#print(columns)
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
	#print(conditions)
	#assuming two conditions only with one logical
	if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
		isIncluded = True
	else:
		isIncluded = False

	tabulated = []
	printDataRecursive(database, column_headers, tabulated, [], table_column, conditions, logicals, not len(columns)>0, isIncluded)
	if len(tabulated)>0:
		print(tabulate(tabulated, headers=column_headers, tablefmt='orgtbl'))
		global row_count
		print("Row Count:", row_count)
		

def checkTables(db_tables):
	for table in InterpreterListener.tables:
		if table not in db_tables:
			raise TableNotFoundError(table)

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

						data_type = table_schema[i][1][table_schema[i][0].index(j[0])]
						if j[3] != data_type:
							if j[3] == "date" and data_type == "string":
								InterpreterListener.conditions[index][3] = "string"
							else:
								raise DataTypeNotMatchError(j[0], data_type, j[2])
						InterpreterListener.conditions[index][0] = i + "." + j[0]
						break
			elif j[3] != "two_var":
				column_name = j[0][j[0].find(".")+1:]
				table_name = j[0][0:j[0].find(".")]

				if column_name in table_schema[table_name][0]:
					column_found = True
				data_type = table_schema[table_name][1][table_schema[table_name][0].index(column_name)]
				if data_type != j[3]:
					if j[3] == "date" and data_type == "string":
						InterpreterListener.conditions[index][3] = "string"
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
					if table_schema[tb_name1][1][col_index_1] != table_schema[tb_name2][1][col_index_2]:
						raise DataTypeNotMatchError(col_name1, table_schema[tb_name1][1][col_index_1], col_name2, table_schema[tb_name2][1][col_index_2])

			if not column_found:
				raise ColumnNotFoundError('too many', 'too many')

def main(argv):
	database = {}
	list_tables = ["sample", "sample2", "person"]
	#index 0 is always the primary key
	table_schema = {"sample":[["a", "b", "c"],["number", "string", "string"]],
					"sample2":[["d", "e", "f"],["number", "string", "string"]],
					"person":[["id", "name", "birthdate"],["number", "string", "date"]]}

	for table in list_tables:
		loadDatabase(database, table)

	input_stream = FileStream(argv[1])
	#input_stream = InputStream(input("Enter sql command: "))
	lexer = MySQLLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = MySQLParser(stream)
	parser.addErrorListener(SQLErrorListener())
	tree = parser.s()
	interpreter = InterpreterListener()
	walker = ParseTreeWalker()
	walker.walk(interpreter, tree)
	

	try:
		if interpreter.command=="select":
			checkTables(list_tables)
			checkColumns(table_schema)
			checkConditions(table_schema)

			printData(database, table_schema)
	except SQLError as e:
		print(e.message)
		print()
	finally:
		print("Command:", InterpreterListener.command)
		print("Columns:", InterpreterListener.columns)
		print("Tables:", InterpreterListener.tables)
		print("Conditions:", InterpreterListener.conditions)
		print("Logicals:", InterpreterListener.logicals)


if __name__ == '__main__':
	main(sys.argv)
