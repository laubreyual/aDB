grammar MySQL;

s : SELECT (WS)+ column (WS)+ FROM (WS)+ table (WS)* (where_c)? ';'  | DELETE (WS)+ FROM (WS)+ table (WS)* (where_c)? ';' | INSERT (WS)+ table ((WS)* PL column_name PR)? (WS)+ VALUES (WS)* PL values_c PR ';' ;

WS : [ \t\r\n];

DOT : '.';

COMMA : ',';

PL : '(';

PR : ')';

NUMBER : [0-9]*(.)?[0-9]+;

STRING :  .*?  ;

INSERT : [Ii][Nn][Ss][Ee][Rr][Tt] (WS)+ [Ii][Nn][Tt][Oo];

VALUES : [Vv][Aa][Ll][Uu][Ee][Ss];

DELETE : [Dd][Ee][Ll][Ee][Tt][Ee];

SELECT : [Ss][Ee][Ll][Ee][Cc][Tt];

WHERE : [Ww][Hh][Ee][Rr][Ee];

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

column_name : (WS)* IDENTIFIER (WS)* (COMMA (WS)* IDENTIFIER)*;

table : IDENTIFIER (COMMA IDENTIFIER)*;

where_c :  WHERE (WS)+ condition;

DOT_IDENTIFIER : DOT IDENTIFIER;

S_CONDITION : IDENTIFIER (DOT_IDENTIFIER)? (WS)* RELATIONAL (WS)* (NUMBER | STRING);

condition : S_CONDITION ((WS)+ LOGICAL (WS)+ S_CONDITION)*;

values_c : (WS)* (NUMBER | STRING) (WS)* (COMMA (WS)* (NUMBER | STRING))*;