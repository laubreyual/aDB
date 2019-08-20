grammar MySQL;

s : SELECT column FROM table where? ';';

WS : [ \t\r\n] -> skip;

DOT : '.';

EQUAL : '=';

COMMA : ',';

NUMBER : [0-9]*.?[0-9]+;

STRING :  .*?  ;

LOGICAL : 'AND' | 'OR';

SELECT : 'SELECT' | 'select';

FROM : 'FROM' | 'from';

IDENTIFIER : [a-zA-Z_]+[a-zA-Z_0-9]* ;

column : '*' | column_name;

column_name : IDENTIFIER (COMMA IDENTIFIER)*;

table : IDENTIFIER (COMMA IDENTIFIER)*;

WHERE_K : 'WHERE' | 'where';

where : WHERE_K condition;

DOT_IDENTIFIER : DOT IDENTIFIER;

S_CONDITION : IDENTIFIER DOT_IDENTIFIER? EQUAL (STRING | NUMBER);

condition : S_CONDITION (LOGICAL S_CONDITION)*;

