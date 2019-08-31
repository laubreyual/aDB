// Generated from MySQL.g4 by ANTLR 4.7.2
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by MySQLParser.
function MySQLListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

MySQLListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
MySQLListener.prototype.constructor = MySQLListener;

// Enter a parse tree produced by MySQLParser#s.
MySQLListener.prototype.enterS = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#s.
MySQLListener.prototype.exitS = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#column.
MySQLListener.prototype.enterColumn = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#column.
MySQLListener.prototype.exitColumn = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#column_name.
MySQLListener.prototype.enterColumn_name = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#column_name.
MySQLListener.prototype.exitColumn_name = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#table.
MySQLListener.prototype.enterTable = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#table.
MySQLListener.prototype.exitTable = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#where_c.
MySQLListener.prototype.enterWhere_c = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#where_c.
MySQLListener.prototype.exitWhere_c = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#condition.
MySQLListener.prototype.enterCondition = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#condition.
MySQLListener.prototype.exitCondition = function(ctx) {
};


// Enter a parse tree produced by MySQLParser#values_c.
MySQLListener.prototype.enterValues_c = function(ctx) {
};

// Exit a parse tree produced by MySQLParser#values_c.
MySQLListener.prototype.exitValues_c = function(ctx) {
};



exports.MySQLListener = MySQLListener;