import sys
from antlr4 import *
from MySQLLexer import MySQLLexer
from MySQLParser import MySQLParser
from MySQLListener import MySQLListener



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
		i = 0
		while True:
			name = ctx.IDENTIFIER(i)
			i+=1
			if name == None:
				break
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
		op = ctx.RELATIONAL()
		
		if ctx.STRING() == None:
			value = int(str(ctx.NUMBER()))
		else:
			value = str(ctx.STRING())
		InterpreterListener.conditions.append((str(variable), str(op), value))
	def exitLogical(self, ctx:MySQLParser.LogicalContext):
		if ctx.AND() != None:
			InterpreterListener.logicals.append("AND")
		elif ctx.OR() != None:
			InterpreterListener.logicals.append("OR")

def main(argv):
	input_stream = FileStream(argv[1])
	lexer = MySQLLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = MySQLParser(stream)
	tree = parser.s()
	interpreter = InterpreterListener()
	walker = ParseTreeWalker()
	walker.walk(interpreter, tree)
	print("Command:", InterpreterListener.command)
	print("Columns:", InterpreterListener.columns)
	print("Tables:", InterpreterListener.tables)
	print("Conditions:", InterpreterListener.conditions)
	print("Logicals:", InterpreterListener.logicals)
 
if __name__ == '__main__':
	main(sys.argv)