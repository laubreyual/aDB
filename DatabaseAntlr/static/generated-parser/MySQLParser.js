// Generated from MySQL.g4 by ANTLR 4.7.2
// jshint ignore: start
var antlr4 = require('antlr4/index');
var MySQLListener = require('./MySQLListener').MySQLListener;
var grammarFileName = "MySQL.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0003\u001b\u00c7\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
    "\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007",
    "\u0004\b\t\b\u0003\u0002\u0003\u0002\u0006\u0002\u0013\n\u0002\r\u0002",
    "\u000e\u0002\u0014\u0003\u0002\u0003\u0002\u0006\u0002\u0019\n\u0002",
    "\r\u0002\u000e\u0002\u001a\u0003\u0002\u0003\u0002\u0006\u0002\u001f",
    "\n\u0002\r\u0002\u000e\u0002 \u0003\u0002\u0003\u0002\u0007\u0002%\n",
    "\u0002\f\u0002\u000e\u0002(\u000b\u0002\u0003\u0002\u0005\u0002+\n\u0002",
    "\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0006\u00021\n\u0002",
    "\r\u0002\u000e\u00022\u0003\u0002\u0003\u0002\u0006\u00027\n\u0002\r",
    "\u0002\u000e\u00028\u0003\u0002\u0003\u0002\u0007\u0002=\n\u0002\f\u0002",
    "\u000e\u0002@\u000b\u0002\u0003\u0002\u0005\u0002C\n\u0002\u0003\u0002",
    "\u0003\u0002\u0003\u0002\u0003\u0002\u0006\u0002I\n\u0002\r\u0002\u000e",
    "\u0002J\u0003\u0002\u0003\u0002\u0007\u0002O\n\u0002\f\u0002\u000e\u0002",
    "R\u000b\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0005",
    "\u0002X\n\u0002\u0003\u0002\u0006\u0002[\n\u0002\r\u0002\u000e\u0002",
    "\\\u0003\u0002\u0003\u0002\u0007\u0002a\n\u0002\f\u0002\u000e\u0002",
    "d\u000b\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0003",
    "\u0002\u0005\u0002k\n\u0002\u0003\u0003\u0003\u0003\u0005\u0003o\n\u0003",
    "\u0003\u0004\u0007\u0004r\n\u0004\f\u0004\u000e\u0004u\u000b\u0004\u0003",
    "\u0004\u0003\u0004\u0007\u0004y\n\u0004\f\u0004\u000e\u0004|\u000b\u0004",
    "\u0003\u0004\u0003\u0004\u0007\u0004\u0080\n\u0004\f\u0004\u000e\u0004",
    "\u0083\u000b\u0004\u0003\u0004\u0007\u0004\u0086\n\u0004\f\u0004\u000e",
    "\u0004\u0089\u000b\u0004\u0003\u0005\u0003\u0005\u0003\u0005\u0007\u0005",
    "\u008e\n\u0005\f\u0005\u000e\u0005\u0091\u000b\u0005\u0003\u0006\u0003",
    "\u0006\u0006\u0006\u0095\n\u0006\r\u0006\u000e\u0006\u0096\u0003\u0006",
    "\u0003\u0006\u0003\u0007\u0003\u0007\u0006\u0007\u009d\n\u0007\r\u0007",
    "\u000e\u0007\u009e\u0003\u0007\u0003\u0007\u0006\u0007\u00a3\n\u0007",
    "\r\u0007\u000e\u0007\u00a4\u0003\u0007\u0007\u0007\u00a8\n\u0007\f\u0007",
    "\u000e\u0007\u00ab\u000b\u0007\u0003\b\u0007\b\u00ae\n\b\f\b\u000e\b",
    "\u00b1\u000b\b\u0003\b\u0003\b\u0007\b\u00b5\n\b\f\b\u000e\b\u00b8\u000b",
    "\b\u0003\b\u0003\b\u0007\b\u00bc\n\b\f\b\u000e\b\u00bf\u000b\b\u0003",
    "\b\u0007\b\u00c2\n\b\f\b\u000e\b\u00c5\u000b\b\u0003\b\u0002\u0002\t",
    "\u0002\u0004\u0006\b\n\f\u000e\u0002\u0003\u0003\u0002\n\u000b\u0002",
    "\u00dd\u0002j\u0003\u0002\u0002\u0002\u0004n\u0003\u0002\u0002\u0002",
    "\u0006s\u0003\u0002\u0002\u0002\b\u008a\u0003\u0002\u0002\u0002\n\u0092",
    "\u0003\u0002\u0002\u0002\f\u009a\u0003\u0002\u0002\u0002\u000e\u00af",
    "\u0003\u0002\u0002\u0002\u0010\u0012\u0007\u000f\u0002\u0002\u0011\u0013",
    "\u0007\u0005\u0002\u0002\u0012\u0011\u0003\u0002\u0002\u0002\u0013\u0014",
    "\u0003\u0002\u0002\u0002\u0014\u0012\u0003\u0002\u0002\u0002\u0014\u0015",
    "\u0003\u0002\u0002\u0002\u0015\u0016\u0003\u0002\u0002\u0002\u0016\u0018",
    "\u0005\u0004\u0003\u0002\u0017\u0019\u0007\u0005\u0002\u0002\u0018\u0017",
    "\u0003\u0002\u0002\u0002\u0019\u001a\u0003\u0002\u0002\u0002\u001a\u0018",
    "\u0003\u0002\u0002\u0002\u001a\u001b\u0003\u0002\u0002\u0002\u001b\u001c",
    "\u0003\u0002\u0002\u0002\u001c\u001e\u0007\u0011\u0002\u0002\u001d\u001f",
    "\u0007\u0005\u0002\u0002\u001e\u001d\u0003\u0002\u0002\u0002\u001f ",
    "\u0003\u0002\u0002\u0002 \u001e\u0003\u0002\u0002\u0002 !\u0003\u0002",
    "\u0002\u0002!\"\u0003\u0002\u0002\u0002\"&\u0005\b\u0005\u0002#%\u0007",
    "\u0005\u0002\u0002$#\u0003\u0002\u0002\u0002%(\u0003\u0002\u0002\u0002",
    "&$\u0003\u0002\u0002\u0002&\'\u0003\u0002\u0002\u0002\'*\u0003\u0002",
    "\u0002\u0002(&\u0003\u0002\u0002\u0002)+\u0005\n\u0006\u0002*)\u0003",
    "\u0002\u0002\u0002*+\u0003\u0002\u0002\u0002+,\u0003\u0002\u0002\u0002",
    ",-\u0007\u0003\u0002\u0002-k\u0003\u0002\u0002\u0002.0\u0007\u000e\u0002",
    "\u0002/1\u0007\u0005\u0002\u00020/\u0003\u0002\u0002\u000212\u0003\u0002",
    "\u0002\u000220\u0003\u0002\u0002\u000223\u0003\u0002\u0002\u000234\u0003",
    "\u0002\u0002\u000246\u0007\u0011\u0002\u000257\u0007\u0005\u0002\u0002",
    "65\u0003\u0002\u0002\u000278\u0003\u0002\u0002\u000286\u0003\u0002\u0002",
    "\u000289\u0003\u0002\u0002\u00029:\u0003\u0002\u0002\u0002:>\u0005\b",
    "\u0005\u0002;=\u0007\u0005\u0002\u0002<;\u0003\u0002\u0002\u0002=@\u0003",
    "\u0002\u0002\u0002><\u0003\u0002\u0002\u0002>?\u0003\u0002\u0002\u0002",
    "?B\u0003\u0002\u0002\u0002@>\u0003\u0002\u0002\u0002AC\u0005\n\u0006",
    "\u0002BA\u0003\u0002\u0002\u0002BC\u0003\u0002\u0002\u0002CD\u0003\u0002",
    "\u0002\u0002DE\u0007\u0003\u0002\u0002Ek\u0003\u0002\u0002\u0002FH\u0007",
    "\f\u0002\u0002GI\u0007\u0005\u0002\u0002HG\u0003\u0002\u0002\u0002I",
    "J\u0003\u0002\u0002\u0002JH\u0003\u0002\u0002\u0002JK\u0003\u0002\u0002",
    "\u0002KL\u0003\u0002\u0002\u0002LW\u0005\b\u0005\u0002MO\u0007\u0005",
    "\u0002\u0002NM\u0003\u0002\u0002\u0002OR\u0003\u0002\u0002\u0002PN\u0003",
    "\u0002\u0002\u0002PQ\u0003\u0002\u0002\u0002QS\u0003\u0002\u0002\u0002",
    "RP\u0003\u0002\u0002\u0002ST\u0007\b\u0002\u0002TU\u0005\u0006\u0004",
    "\u0002UV\u0007\t\u0002\u0002VX\u0003\u0002\u0002\u0002WP\u0003\u0002",
    "\u0002\u0002WX\u0003\u0002\u0002\u0002XZ\u0003\u0002\u0002\u0002Y[\u0007",
    "\u0005\u0002\u0002ZY\u0003\u0002\u0002\u0002[\\\u0003\u0002\u0002\u0002",
    "\\Z\u0003\u0002\u0002\u0002\\]\u0003\u0002\u0002\u0002]^\u0003\u0002",
    "\u0002\u0002^b\u0007\r\u0002\u0002_a\u0007\u0005\u0002\u0002`_\u0003",
    "\u0002\u0002\u0002ad\u0003\u0002\u0002\u0002b`\u0003\u0002\u0002\u0002",
    "bc\u0003\u0002\u0002\u0002ce\u0003\u0002\u0002\u0002db\u0003\u0002\u0002",
    "\u0002ef\u0007\b\u0002\u0002fg\u0005\u000e\b\u0002gh\u0007\t\u0002\u0002",
    "hi\u0007\u0003\u0002\u0002ik\u0003\u0002\u0002\u0002j\u0010\u0003\u0002",
    "\u0002\u0002j.\u0003\u0002\u0002\u0002jF\u0003\u0002\u0002\u0002k\u0003",
    "\u0003\u0002\u0002\u0002lo\u0007\u0004\u0002\u0002mo\u0005\u0006\u0004",
    "\u0002nl\u0003\u0002\u0002\u0002nm\u0003\u0002\u0002\u0002o\u0005\u0003",
    "\u0002\u0002\u0002pr\u0007\u0005\u0002\u0002qp\u0003\u0002\u0002\u0002",
    "ru\u0003\u0002\u0002\u0002sq\u0003\u0002\u0002\u0002st\u0003\u0002\u0002",
    "\u0002tv\u0003\u0002\u0002\u0002us\u0003\u0002\u0002\u0002vz\u0007\u0019",
    "\u0002\u0002wy\u0007\u0005\u0002\u0002xw\u0003\u0002\u0002\u0002y|\u0003",
    "\u0002\u0002\u0002zx\u0003\u0002\u0002\u0002z{\u0003\u0002\u0002\u0002",
    "{\u0087\u0003\u0002\u0002\u0002|z\u0003\u0002\u0002\u0002}\u0081\u0007",
    "\u0007\u0002\u0002~\u0080\u0007\u0005\u0002\u0002\u007f~\u0003\u0002",
    "\u0002\u0002\u0080\u0083\u0003\u0002\u0002\u0002\u0081\u007f\u0003\u0002",
    "\u0002\u0002\u0081\u0082\u0003\u0002\u0002\u0002\u0082\u0084\u0003\u0002",
    "\u0002\u0002\u0083\u0081\u0003\u0002\u0002\u0002\u0084\u0086\u0007\u0019",
    "\u0002\u0002\u0085}\u0003\u0002\u0002\u0002\u0086\u0089\u0003\u0002",
    "\u0002\u0002\u0087\u0085\u0003\u0002\u0002\u0002\u0087\u0088\u0003\u0002",
    "\u0002\u0002\u0088\u0007\u0003\u0002\u0002\u0002\u0089\u0087\u0003\u0002",
    "\u0002\u0002\u008a\u008f\u0007\u0019\u0002\u0002\u008b\u008c\u0007\u0007",
    "\u0002\u0002\u008c\u008e\u0007\u0019\u0002\u0002\u008d\u008b\u0003\u0002",
    "\u0002\u0002\u008e\u0091\u0003\u0002\u0002\u0002\u008f\u008d\u0003\u0002",
    "\u0002\u0002\u008f\u0090\u0003\u0002\u0002\u0002\u0090\t\u0003\u0002",
    "\u0002\u0002\u0091\u008f\u0003\u0002\u0002\u0002\u0092\u0094\u0007\u0010",
    "\u0002\u0002\u0093\u0095\u0007\u0005\u0002\u0002\u0094\u0093\u0003\u0002",
    "\u0002\u0002\u0095\u0096\u0003\u0002\u0002\u0002\u0096\u0094\u0003\u0002",
    "\u0002\u0002\u0096\u0097\u0003\u0002\u0002\u0002\u0097\u0098\u0003\u0002",
    "\u0002\u0002\u0098\u0099\u0005\f\u0007\u0002\u0099\u000b\u0003\u0002",
    "\u0002\u0002\u009a\u00a9\u0007\u001b\u0002\u0002\u009b\u009d\u0007\u0005",
    "\u0002\u0002\u009c\u009b\u0003\u0002\u0002\u0002\u009d\u009e\u0003\u0002",
    "\u0002\u0002\u009e\u009c\u0003\u0002\u0002\u0002\u009e\u009f\u0003\u0002",
    "\u0002\u0002\u009f\u00a0\u0003\u0002\u0002\u0002\u00a0\u00a2\u0007\u0018",
    "\u0002\u0002\u00a1\u00a3\u0007\u0005\u0002\u0002\u00a2\u00a1\u0003\u0002",
    "\u0002\u0002\u00a3\u00a4\u0003\u0002\u0002\u0002\u00a4\u00a2\u0003\u0002",
    "\u0002\u0002\u00a4\u00a5\u0003\u0002\u0002\u0002\u00a5\u00a6\u0003\u0002",
    "\u0002\u0002\u00a6\u00a8\u0007\u001b\u0002\u0002\u00a7\u009c\u0003\u0002",
    "\u0002\u0002\u00a8\u00ab\u0003\u0002\u0002\u0002\u00a9\u00a7\u0003\u0002",
    "\u0002\u0002\u00a9\u00aa\u0003\u0002\u0002\u0002\u00aa\r\u0003\u0002",
    "\u0002\u0002\u00ab\u00a9\u0003\u0002\u0002\u0002\u00ac\u00ae\u0007\u0005",
    "\u0002\u0002\u00ad\u00ac\u0003\u0002\u0002\u0002\u00ae\u00b1\u0003\u0002",
    "\u0002\u0002\u00af\u00ad\u0003\u0002\u0002\u0002\u00af\u00b0\u0003\u0002",
    "\u0002\u0002\u00b0\u00b2\u0003\u0002\u0002\u0002\u00b1\u00af\u0003\u0002",
    "\u0002\u0002\u00b2\u00b6\t\u0002\u0002\u0002\u00b3\u00b5\u0007\u0005",
    "\u0002\u0002\u00b4\u00b3\u0003\u0002\u0002\u0002\u00b5\u00b8\u0003\u0002",
    "\u0002\u0002\u00b6\u00b4\u0003\u0002\u0002\u0002\u00b6\u00b7\u0003\u0002",
    "\u0002\u0002\u00b7\u00c3\u0003\u0002\u0002\u0002\u00b8\u00b6\u0003\u0002",
    "\u0002\u0002\u00b9\u00bd\u0007\u0007\u0002\u0002\u00ba\u00bc\u0007\u0005",
    "\u0002\u0002\u00bb\u00ba\u0003\u0002\u0002\u0002\u00bc\u00bf\u0003\u0002",
    "\u0002\u0002\u00bd\u00bb\u0003\u0002\u0002\u0002\u00bd\u00be\u0003\u0002",
    "\u0002\u0002\u00be\u00c0\u0003\u0002\u0002\u0002\u00bf\u00bd\u0003\u0002",
    "\u0002\u0002\u00c0\u00c2\t\u0002\u0002\u0002\u00c1\u00b9\u0003\u0002",
    "\u0002\u0002\u00c2\u00c5\u0003\u0002\u0002\u0002\u00c3\u00c1\u0003\u0002",
    "\u0002\u0002\u00c3\u00c4\u0003\u0002\u0002\u0002\u00c4\u000f\u0003\u0002",
    "\u0002\u0002\u00c5\u00c3\u0003\u0002\u0002\u0002\u001f\u0014\u001a ",
    "&*28>BJPW\\bjnsz\u0081\u0087\u008f\u0096\u009e\u00a4\u00a9\u00af\u00b6",
    "\u00bd\u00c3"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, "';'", "'*'", null, "'.'", "','", "'('", "')'" ];

var symbolicNames = [ null, null, null, "WS", "DOT", "COMMA", "PL", "PR", 
                      "NUMBER", "STRING", "INSERT", "VALUES", "DELETE", 
                      "SELECT", "WHERE", "FROM", "BETWEEN", "LIKE", "IN", 
                      "RELATIONAL", "AND", "OR", "LOGICAL", "IDENTIFIER", 
                      "DOT_IDENTIFIER", "S_CONDITION" ];

var ruleNames =  [ "s", "column", "column_name", "table", "where_c", "condition", 
                   "values_c" ];

function MySQLParser (input) {
	antlr4.Parser.call(this, input);
    this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
    this.ruleNames = ruleNames;
    this.literalNames = literalNames;
    this.symbolicNames = symbolicNames;
    return this;
}

MySQLParser.prototype = Object.create(antlr4.Parser.prototype);
MySQLParser.prototype.constructor = MySQLParser;

Object.defineProperty(MySQLParser.prototype, "atn", {
	get : function() {
		return atn;
	}
});

MySQLParser.EOF = antlr4.Token.EOF;
MySQLParser.T__0 = 1;
MySQLParser.T__1 = 2;
MySQLParser.WS = 3;
MySQLParser.DOT = 4;
MySQLParser.COMMA = 5;
MySQLParser.PL = 6;
MySQLParser.PR = 7;
MySQLParser.NUMBER = 8;
MySQLParser.STRING = 9;
MySQLParser.INSERT = 10;
MySQLParser.VALUES = 11;
MySQLParser.DELETE = 12;
MySQLParser.SELECT = 13;
MySQLParser.WHERE = 14;
MySQLParser.FROM = 15;
MySQLParser.BETWEEN = 16;
MySQLParser.LIKE = 17;
MySQLParser.IN = 18;
MySQLParser.RELATIONAL = 19;
MySQLParser.AND = 20;
MySQLParser.OR = 21;
MySQLParser.LOGICAL = 22;
MySQLParser.IDENTIFIER = 23;
MySQLParser.DOT_IDENTIFIER = 24;
MySQLParser.S_CONDITION = 25;

MySQLParser.RULE_s = 0;
MySQLParser.RULE_column = 1;
MySQLParser.RULE_column_name = 2;
MySQLParser.RULE_table = 3;
MySQLParser.RULE_where_c = 4;
MySQLParser.RULE_condition = 5;
MySQLParser.RULE_values_c = 6;


function SContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_s;
    return this;
}

SContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
SContext.prototype.constructor = SContext;

SContext.prototype.SELECT = function() {
    return this.getToken(MySQLParser.SELECT, 0);
};

SContext.prototype.column = function() {
    return this.getTypedRuleContext(ColumnContext,0);
};

SContext.prototype.FROM = function() {
    return this.getToken(MySQLParser.FROM, 0);
};

SContext.prototype.table = function() {
    return this.getTypedRuleContext(TableContext,0);
};

SContext.prototype.WS = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.WS);
    } else {
        return this.getToken(MySQLParser.WS, i);
    }
};


SContext.prototype.where_c = function() {
    return this.getTypedRuleContext(Where_cContext,0);
};

SContext.prototype.DELETE = function() {
    return this.getToken(MySQLParser.DELETE, 0);
};

SContext.prototype.INSERT = function() {
    return this.getToken(MySQLParser.INSERT, 0);
};

SContext.prototype.VALUES = function() {
    return this.getToken(MySQLParser.VALUES, 0);
};

SContext.prototype.PL = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.PL);
    } else {
        return this.getToken(MySQLParser.PL, i);
    }
};


SContext.prototype.values_c = function() {
    return this.getTypedRuleContext(Values_cContext,0);
};

SContext.prototype.PR = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.PR);
    } else {
        return this.getToken(MySQLParser.PR, i);
    }
};


SContext.prototype.column_name = function() {
    return this.getTypedRuleContext(Column_nameContext,0);
};

SContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterS(this);
	}
};

SContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitS(this);
	}
};




MySQLParser.SContext = SContext;

MySQLParser.prototype.s = function() {

    var localctx = new SContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, MySQLParser.RULE_s);
    var _la = 0; // Token type
    try {
        this.state = 104;
        this._errHandler.sync(this);
        switch(this._input.LA(1)) {
        case MySQLParser.SELECT:
            this.enterOuterAlt(localctx, 1);
            this.state = 14;
            this.match(MySQLParser.SELECT);
            this.state = 16; 
            this._errHandler.sync(this);
            var _alt = 1;
            do {
            	switch (_alt) {
            	case 1:
            		this.state = 15;
            		this.match(MySQLParser.WS);
            		break;
            	default:
            		throw new antlr4.error.NoViableAltException(this);
            	}
            	this.state = 18; 
            	this._errHandler.sync(this);
            	_alt = this._interp.adaptivePredict(this._input,0, this._ctx);
            } while ( _alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER );
            this.state = 20;
            this.column();
            this.state = 22; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 21;
                this.match(MySQLParser.WS);
                this.state = 24; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 26;
            this.match(MySQLParser.FROM);
            this.state = 28; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 27;
                this.match(MySQLParser.WS);
                this.state = 30; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 32;
            this.table();
            this.state = 36;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            while(_la===MySQLParser.WS) {
                this.state = 33;
                this.match(MySQLParser.WS);
                this.state = 38;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            }
            this.state = 40;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if(_la===MySQLParser.WHERE) {
                this.state = 39;
                this.where_c();
            }

            this.state = 42;
            this.match(MySQLParser.T__0);
            break;
        case MySQLParser.DELETE:
            this.enterOuterAlt(localctx, 2);
            this.state = 44;
            this.match(MySQLParser.DELETE);
            this.state = 46; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 45;
                this.match(MySQLParser.WS);
                this.state = 48; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 50;
            this.match(MySQLParser.FROM);
            this.state = 52; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 51;
                this.match(MySQLParser.WS);
                this.state = 54; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 56;
            this.table();
            this.state = 60;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            while(_la===MySQLParser.WS) {
                this.state = 57;
                this.match(MySQLParser.WS);
                this.state = 62;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            }
            this.state = 64;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if(_la===MySQLParser.WHERE) {
                this.state = 63;
                this.where_c();
            }

            this.state = 66;
            this.match(MySQLParser.T__0);
            break;
        case MySQLParser.INSERT:
            this.enterOuterAlt(localctx, 3);
            this.state = 68;
            this.match(MySQLParser.INSERT);
            this.state = 70; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 69;
                this.match(MySQLParser.WS);
                this.state = 72; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 74;
            this.table();
            this.state = 85;
            this._errHandler.sync(this);
            var la_ = this._interp.adaptivePredict(this._input,11,this._ctx);
            if(la_===1) {
                this.state = 78;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
                while(_la===MySQLParser.WS) {
                    this.state = 75;
                    this.match(MySQLParser.WS);
                    this.state = 80;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                }
                this.state = 81;
                this.match(MySQLParser.PL);
                this.state = 82;
                this.column_name();
                this.state = 83;
                this.match(MySQLParser.PR);

            }
            this.state = 88; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 87;
                this.match(MySQLParser.WS);
                this.state = 90; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 92;
            this.match(MySQLParser.VALUES);
            this.state = 96;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            while(_la===MySQLParser.WS) {
                this.state = 93;
                this.match(MySQLParser.WS);
                this.state = 98;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            }
            this.state = 99;
            this.match(MySQLParser.PL);
            this.state = 100;
            this.values_c();
            this.state = 101;
            this.match(MySQLParser.PR);
            this.state = 102;
            this.match(MySQLParser.T__0);
            break;
        default:
            throw new antlr4.error.NoViableAltException(this);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function ColumnContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_column;
    return this;
}

ColumnContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ColumnContext.prototype.constructor = ColumnContext;

ColumnContext.prototype.column_name = function() {
    return this.getTypedRuleContext(Column_nameContext,0);
};

ColumnContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterColumn(this);
	}
};

ColumnContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitColumn(this);
	}
};




MySQLParser.ColumnContext = ColumnContext;

MySQLParser.prototype.column = function() {

    var localctx = new ColumnContext(this, this._ctx, this.state);
    this.enterRule(localctx, 2, MySQLParser.RULE_column);
    try {
        this.state = 108;
        this._errHandler.sync(this);
        switch(this._input.LA(1)) {
        case MySQLParser.T__1:
            this.enterOuterAlt(localctx, 1);
            this.state = 106;
            this.match(MySQLParser.T__1);
            break;
        case MySQLParser.WS:
        case MySQLParser.IDENTIFIER:
            this.enterOuterAlt(localctx, 2);
            this.state = 107;
            this.column_name();
            break;
        default:
            throw new antlr4.error.NoViableAltException(this);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function Column_nameContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_column_name;
    return this;
}

Column_nameContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
Column_nameContext.prototype.constructor = Column_nameContext;

Column_nameContext.prototype.IDENTIFIER = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.IDENTIFIER);
    } else {
        return this.getToken(MySQLParser.IDENTIFIER, i);
    }
};


Column_nameContext.prototype.WS = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.WS);
    } else {
        return this.getToken(MySQLParser.WS, i);
    }
};


Column_nameContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.COMMA);
    } else {
        return this.getToken(MySQLParser.COMMA, i);
    }
};


Column_nameContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterColumn_name(this);
	}
};

Column_nameContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitColumn_name(this);
	}
};




MySQLParser.Column_nameContext = Column_nameContext;

MySQLParser.prototype.column_name = function() {

    var localctx = new Column_nameContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, MySQLParser.RULE_column_name);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 113;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.WS) {
            this.state = 110;
            this.match(MySQLParser.WS);
            this.state = 115;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 116;
        this.match(MySQLParser.IDENTIFIER);
        this.state = 120;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,17,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 117;
                this.match(MySQLParser.WS); 
            }
            this.state = 122;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,17,this._ctx);
        }

        this.state = 133;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.COMMA) {
            this.state = 123;
            this.match(MySQLParser.COMMA);
            this.state = 127;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            while(_la===MySQLParser.WS) {
                this.state = 124;
                this.match(MySQLParser.WS);
                this.state = 129;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            }
            this.state = 130;
            this.match(MySQLParser.IDENTIFIER);
            this.state = 135;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function TableContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_table;
    return this;
}

TableContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TableContext.prototype.constructor = TableContext;

TableContext.prototype.IDENTIFIER = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.IDENTIFIER);
    } else {
        return this.getToken(MySQLParser.IDENTIFIER, i);
    }
};


TableContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.COMMA);
    } else {
        return this.getToken(MySQLParser.COMMA, i);
    }
};


TableContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterTable(this);
	}
};

TableContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitTable(this);
	}
};




MySQLParser.TableContext = TableContext;

MySQLParser.prototype.table = function() {

    var localctx = new TableContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, MySQLParser.RULE_table);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 136;
        this.match(MySQLParser.IDENTIFIER);
        this.state = 141;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.COMMA) {
            this.state = 137;
            this.match(MySQLParser.COMMA);
            this.state = 138;
            this.match(MySQLParser.IDENTIFIER);
            this.state = 143;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function Where_cContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_where_c;
    return this;
}

Where_cContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
Where_cContext.prototype.constructor = Where_cContext;

Where_cContext.prototype.WHERE = function() {
    return this.getToken(MySQLParser.WHERE, 0);
};

Where_cContext.prototype.condition = function() {
    return this.getTypedRuleContext(ConditionContext,0);
};

Where_cContext.prototype.WS = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.WS);
    } else {
        return this.getToken(MySQLParser.WS, i);
    }
};


Where_cContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterWhere_c(this);
	}
};

Where_cContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitWhere_c(this);
	}
};




MySQLParser.Where_cContext = Where_cContext;

MySQLParser.prototype.where_c = function() {

    var localctx = new Where_cContext(this, this._ctx, this.state);
    this.enterRule(localctx, 8, MySQLParser.RULE_where_c);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 144;
        this.match(MySQLParser.WHERE);
        this.state = 146; 
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        do {
            this.state = 145;
            this.match(MySQLParser.WS);
            this.state = 148; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        } while(_la===MySQLParser.WS);
        this.state = 150;
        this.condition();
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function ConditionContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_condition;
    return this;
}

ConditionContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ConditionContext.prototype.constructor = ConditionContext;

ConditionContext.prototype.S_CONDITION = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.S_CONDITION);
    } else {
        return this.getToken(MySQLParser.S_CONDITION, i);
    }
};


ConditionContext.prototype.LOGICAL = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.LOGICAL);
    } else {
        return this.getToken(MySQLParser.LOGICAL, i);
    }
};


ConditionContext.prototype.WS = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.WS);
    } else {
        return this.getToken(MySQLParser.WS, i);
    }
};


ConditionContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterCondition(this);
	}
};

ConditionContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitCondition(this);
	}
};




MySQLParser.ConditionContext = ConditionContext;

MySQLParser.prototype.condition = function() {

    var localctx = new ConditionContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, MySQLParser.RULE_condition);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 152;
        this.match(MySQLParser.S_CONDITION);
        this.state = 167;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.WS) {
            this.state = 154; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 153;
                this.match(MySQLParser.WS);
                this.state = 156; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 158;
            this.match(MySQLParser.LOGICAL);
            this.state = 160; 
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            do {
                this.state = 159;
                this.match(MySQLParser.WS);
                this.state = 162; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            } while(_la===MySQLParser.WS);
            this.state = 164;
            this.match(MySQLParser.S_CONDITION);
            this.state = 169;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function Values_cContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = MySQLParser.RULE_values_c;
    return this;
}

Values_cContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
Values_cContext.prototype.constructor = Values_cContext;

Values_cContext.prototype.NUMBER = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.NUMBER);
    } else {
        return this.getToken(MySQLParser.NUMBER, i);
    }
};


Values_cContext.prototype.STRING = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.STRING);
    } else {
        return this.getToken(MySQLParser.STRING, i);
    }
};


Values_cContext.prototype.WS = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.WS);
    } else {
        return this.getToken(MySQLParser.WS, i);
    }
};


Values_cContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(MySQLParser.COMMA);
    } else {
        return this.getToken(MySQLParser.COMMA, i);
    }
};


Values_cContext.prototype.enterRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.enterValues_c(this);
	}
};

Values_cContext.prototype.exitRule = function(listener) {
    if(listener instanceof MySQLListener ) {
        listener.exitValues_c(this);
	}
};




MySQLParser.Values_cContext = Values_cContext;

MySQLParser.prototype.values_c = function() {

    var localctx = new Values_cContext(this, this._ctx, this.state);
    this.enterRule(localctx, 12, MySQLParser.RULE_values_c);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 173;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.WS) {
            this.state = 170;
            this.match(MySQLParser.WS);
            this.state = 175;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 176;
        _la = this._input.LA(1);
        if(!(_la===MySQLParser.NUMBER || _la===MySQLParser.STRING)) {
        this._errHandler.recoverInline(this);
        }
        else {
        	this._errHandler.reportMatch(this);
            this.consume();
        }
        this.state = 180;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.WS) {
            this.state = 177;
            this.match(MySQLParser.WS);
            this.state = 182;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 193;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===MySQLParser.COMMA) {
            this.state = 183;
            this.match(MySQLParser.COMMA);
            this.state = 187;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            while(_la===MySQLParser.WS) {
                this.state = 184;
                this.match(MySQLParser.WS);
                this.state = 189;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
            }
            this.state = 190;
            _la = this._input.LA(1);
            if(!(_la===MySQLParser.NUMBER || _la===MySQLParser.STRING)) {
            this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            this.state = 195;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


exports.MySQLParser = MySQLParser;
