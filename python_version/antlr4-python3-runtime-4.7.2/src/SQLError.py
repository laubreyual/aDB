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
			self.message = 'Data type did not match. "{}" is of TYPE "{}", while "{}" is TYPE "{}".'.format(attrib, data_type, value, data_type2)
		super().__init__(self.message)

class InvalidStringLengthError(SQLError):
	def __init__(self, value, attrib, length):
		self.message = '"{}" length is greater than the prescribed length of "{}" ({}).'.format(value, attrib, length)
		super().__init__(self.message)

class PrimaryKeyAlreadyExistsError(SQLError):
	def __init__(self, value, table):
		self.message = '"{}" is already a primary key in TABLE "{}".'.format(value, table)
		super().__init__(self.message)

class IncorrectPrimaryKeyError(SQLError):
	def __init__(self, value, table):
		self.message = '"{}" is not the primary key in TABLE "{}".'.format(value, table)
		super().__init__(self.message)

class TableFoundError(SQLError):
	def __init__(self, table):
		self.message = 'TABLE "{}" already exists.'.format(table)
		super().__init__(self.message)

class DataTypeNotFound(SQLError):
	def __init__(self, data_type):
		self.message = 'DATATYPE "{}" does not exist.'.format(data_type)
		super().__init__(self.message)

class StringSizeError(SQLError):
	def __init__(self):
		self.message = 'Invalid size for STRING(length). `length` should be between 0 to 300.'
		super().__init__(self.message)

class FloatSizeError(SQLError):
	def __init__(self, typeof):
		self.message = 'Invalid size for FLOAT(digits, precisions).'

		if typeof == 'larger':
			self.message = self.message + ' `digits` should be greater than `precisions`.'
		elif typeof == 'digits':
			self.message = self.message + ' `digits` should be between 1 to 9.'
		elif typeof == 'precisions':
			self.message = self.message + ' `precisions` should be between 0 to 4.'

		super().__init__(self.message)

class InvalidDateError(SQLError):
	def __init__(self, date):
		self.message = 'Invalid date.'
		super().__init__(self.message)

class InvalidFloatError(SQLError):
	def __init__(self, number, restrictions, typeof):
		self.message = 'Invalid value for float FLOAT{}.'.format(restrictions)

		if typeof == 'limit':
			self.message = self.message + ' value must be between -65000 and 65000.'

		super().__init__(self.message)
