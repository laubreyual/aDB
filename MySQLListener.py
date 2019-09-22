# Generated from MySQL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySQLParser import MySQLParser
else:
    from MySQLParser import MySQLParser

# This class defines a complete listener for a parse tree produced by MySQLParser.
class MySQLListener(ParseTreeListener):

    # Enter a parse tree produced by MySQLParser#s.
    def enterS(self, ctx:MySQLParser.SContext):
        pass

    # Exit a parse tree produced by MySQLParser#s.
    def exitS(self, ctx:MySQLParser.SContext):
        pass


    # Enter a parse tree produced by MySQLParser#column.
    def enterColumn(self, ctx:MySQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by MySQLParser#column.
    def exitColumn(self, ctx:MySQLParser.ColumnContext):
        pass


    # Enter a parse tree produced by MySQLParser#column_name.
    def enterColumn_name(self, ctx:MySQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by MySQLParser#column_name.
    def exitColumn_name(self, ctx:MySQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by MySQLParser#table.
    def enterTable(self, ctx:MySQLParser.TableContext):
        pass

    # Exit a parse tree produced by MySQLParser#table.
    def exitTable(self, ctx:MySQLParser.TableContext):
        pass


    # Enter a parse tree produced by MySQLParser#where_c.
    def enterWhere_c(self, ctx:MySQLParser.Where_cContext):
        pass

    # Exit a parse tree produced by MySQLParser#where_c.
    def exitWhere_c(self, ctx:MySQLParser.Where_cContext):
        pass


    # Enter a parse tree produced by MySQLParser#condition.
    def enterCondition(self, ctx:MySQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by MySQLParser#condition.
    def exitCondition(self, ctx:MySQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by MySQLParser#values_c.
    def enterValues_c(self, ctx:MySQLParser.Values_cContext):
        pass

    # Exit a parse tree produced by MySQLParser#values_c.
    def exitValues_c(self, ctx:MySQLParser.Values_cContext):
        pass


    # Enter a parse tree produced by MySQLParser#attributes.
    def enterAttributes(self, ctx:MySQLParser.AttributesContext):
        pass

    # Exit a parse tree produced by MySQLParser#attributes.
    def exitAttributes(self, ctx:MySQLParser.AttributesContext):
        pass


