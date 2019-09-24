import sys
from antlr4 import *
from MySQLLexer import MySQLLexer
from MySQLParser import MySQLParser
from MySQLListener import MySQLListener
from BTrees.OOBTree import OOBTree
from DatabasePY import *
from antlr4.error.ErrorListener import ErrorListener

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
		variable = ctx.IDENTIFIER()
		dot_name = ctx.DOT_IDENTIFIER()
		op = ctx.RELATIONAL()
		if dot_name != None:
			variable = str(variable) + str(dot_name)

		if ctx.NUMBER() != None:
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

def printDataRecursive(database, l, table_column, conditions, logicals, isPrintAll, isIncluded):
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
				if condition[0] == table[0]:
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
			printDataRecursive(database, l+to_print, table_column[1:], conditions, logicals, isPrintAll, isIncluded_new)
	elif isIncluded:
		print(l)


def printData(database, table_schema):
	tables = InterpreterListener.tables
	columns = InterpreterListener.columns
	conditions = InterpreterListener.conditions
	logicals = InterpreterListener.logicals

	#print the column header
	if len(columns) > 0:
		print(columns)
	else: # the column specified was *
		temp = []
		for table in tables:
			temp += table_schema[table][0]
		print(temp)


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
	#print(conditions)
	#assuming two conditions only with one logical
	if len(logicals)==0 or (len(logicals)!=0 and logicals[0] == 'AND'):
		isIncluded = True
	else:
		isIncluded = False
	printDataRecursive(database, [], table_column, conditions, logicals, not len(columns)>0, isIncluded)

def main(argv):
	database = {}
	list_tables = ["sample", "sample2"]
	#index 0 is always the primary key
	table_schema = {"sample":[["a", "b", "c"],["number", "string", "string"]],
					"sample2":[["d", "e", "f"],["number", "string", "string"]]}

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
	

	if InterpreterListener.command=="select":
		
		#error checking
		error = False

		#error checking in tables
		for i in InterpreterListener.tables:
			if i not in list_tables:
				print("Error: table", i, "does not exist")
				error = True
				break
		#error checking in columns
		for index in range(0, len(InterpreterListener.columns)):
			j = InterpreterListener.columns[index]
			column_found = False
			if "." not in j:
				for i in InterpreterListener.tables:
					if j in table_schema[i][0]:
						column_found = True
						InterpreterListener.columns[index] = i + "." + j
						break
			else:
				if j[j.find(".")+1:] in table_schema[j[0:j.find(".")]][0]:
					column_found = True
			if not column_found:
				print("Error: column", j, "does not exist")
				error = True
		#error checking in conditions
		for index in range(0, len(InterpreterListener.conditions)):
			j = InterpreterListener.conditions[index]
			# j[0] = condition variable
			column_found = False
			if "." not in j[0]:
				for i in InterpreterListener.tables:
					if j[0] in table_schema[i][0]:
						column_found = True
						#check data type

						data_type = table_schema[i][1][table_schema[i][0].index(j[0])]
						if j[3] != data_type:
							if j[3] == "date" and data_type == "string":
								InterpreterListener.conditions[index][3] = "string"
							else:
								print("Error: wrong data type in the where clause")
								error = True
						InterpreterListener.conditions[index][0] = i + "." + j[0]
						break
			else:
				column_name = j[0][j[0].find(".")+1:]
				table_name = j[0][0:j[0].find(".")]
				
				if column_name in table_schema[table_name][0]:
					column_found = True
				data_type = table_schema[table_name][1][table_schema[table_name][0].index(column_name)]
				if data_type != j[3]:
					if j[3] == "date" and data_type == "string":
						InterpreterListener.conditions[index][3] = "string"
					else:
						print("Error: wrong data type in the where clause")
						error = True
			if not column_found:
				print("Error: column", j[0], "in the where clause does not exist")
				error = True
		#sort conditions
		# for index in range(0)
		#additional error checking here

		#execution of the SQL Statement
		if InterpreterListener.command == 'select' and not error:
			# pass
			printData(database, table_schema)

	print("Command:", InterpreterListener.command)
	print("Columns:", InterpreterListener.columns)
	print("Tables:", InterpreterListener.tables)
	print("Conditions:", InterpreterListener.conditions)
	print("Logicals:", InterpreterListener.logicals)
if __name__ == '__main__':
	main(sys.argv)