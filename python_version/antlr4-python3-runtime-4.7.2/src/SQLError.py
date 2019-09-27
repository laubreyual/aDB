class SQLError(Exception):
	#https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
	pass

class TableNotFoundError(SQLError):
	def __init__(self, table):
		self.message = 'TABLE "{}" does not exist.'.format(table)
		super().__init__(self.message)

class ColumnNotFoundError(SQLError):
	def __init__(self, column, table):
		self.message = 'COLUMN "{}" does not exist in TABLE "{}".'.format(column,table)
		super().__init__(self.message)

class DataTypeNotMatchError(SQLError):
	def __init__(self, attrib, data_type, value, data_type2=''):
		self.message = 'Data type did not match in condition. "{}" is of TYPE "{}", while "{}" is not'.format(attrib, data_type, value)

		if data_type2:
			self.message = 'Data type did not match in condition. "{}" is of TYPE "{}", while "{}" is TYPE "{}".'.format(attrib, data_type, value, data_type2)
		super().__init__(self.message)
