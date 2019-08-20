grammar MySQL;

s : SELECT column FROM table where? ';';

WS : [ \t\r\n] -> skip;

DOT : '.';

COMMA : ',';

NUMBER : [0-9]*.?[0-9]+;

STRING :  .*?  ;

SELECT : [Ss][Ee][Ll][Ee][Cc][Tt];

FROM : [Ff][Rr][Oo][Mm];

BETWEEN : [Bb][Ee][Tt][Ww][Ee][Ee][Nn];

LIKE : [Ll][Ii][Kk][Ee];

IN : [Ii][Nn];

RELATIONAL : '=' | '>' | '<' | '>=' | '<=' | '!=' | BETWEEN | LIKE | IN ;

AND : [Aa][Nn][Dd];

OR : [Oo][Rr];

LOGICAL : AND | OR;

IDENTIFIER : [a-zA-Z_]+[a-zA-Z_0-9]* ;

column : '*' | column_name;

column_name : IDENTIFIER (COMMA IDENTIFIER)*;

table : IDENTIFIER (COMMA IDENTIFIER)*;

WHERE_K : [Ww][Hh][Ee][Rr][Ee];

where : WHERE_K condition;

DOT_IDENTIFIER : DOT IDENTIFIER;

S_CONDITION : IDENTIFIER DOT_IDENTIFIER? RELATIONAL (STRING | NUMBER);

condition : S_CONDITION (LOGICAL S_CONDITION)*;

