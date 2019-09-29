grammar MySQL;

s : select_c | delete_c | insert_c | create_c | describe_c | exit_c;

select_c : SELECT (WS)+ column (WS)+ FROM (WS)+ table (WS)* (where_c)? (WS)* ';' ;

delete_c : DELETE (WS)+ FROM (WS)+ table (WS)* (where_c)? (WS)* ';' ;

insert_c : INSERT (WS)+ table ((WS)* PL column_name PR)? (WS)+ VALUES (WS)* PL values_c PR ';' (WS)* ;

create_c : CREATE (WS)+ table (WS)* PL (WS)* attributes (WS)* PR (WS)*';' ;

EXIT : [Ee][Xx][Ii][Tt] (WS)* ;

exit_c : EXIT ';' ;

WS : [ \t\r\n];

DOT : '.';

COMMA : ',';

PL : '(';

PR : ')';

NUMBER : [0-9]*[.]?[0-9]+;

DATE : ['][0-9][0-9][0-9][0-9]'-'[0-9][0-9]'-'[0-9][0-9]['] | ["][0-9][0-9][0-9][0-9]'-'[0-9][0-9]'-'[0-9][0-9]["];

STRING :  ['] (.)*? ['] | ["] (.)*? ["]  ;

INSERT : [Ii][Nn][Ss][Ee][Rr][Tt] (WS)+ [Ii][Nn][Tt][Oo];

VALUES : [Vv][Aa][Ll][Uu][Ee][Ss];

DELETE : [Dd][Ee][Ll][Ee][Tt][Ee];

SELECT : [Ss][Ee][Ll][Ee][Cc][Tt];

CREATE : [Cc][Rr][Ee][Aa][Tt][Ee] (WS)+ [Tt][Aa][Bb][Ll][Ee];

DESCRIBE : [Dd][Ee][Ss][Cc][Rr][Ii][Bb][Ee];

WHERE : [Ww][Hh][Ee][Rr][Ee];

FROM : [Ff][Rr][Oo][Mm];

BETWEEN : [Bb][Ee][Tt][Ww][Ee][Ee][Nn];

LIKE : [Ll][Ii][Kk][Ee];

IN : [Ii][Nn];

VARCHAR : [Vv][Aa][Rr][Cc][Hh][Aa][Rr] (WS)* PL (WS)* NUMBER (WS)* PR;

INT : [Ii][Nn][Tt] (WS)* PL (WS)* NUMBER (WS)* PR;

V_DATE : [Dd][Aa][Tt][Ee];

PRIMARY : [Pp][Rr][Ii][Mm][Aa][Rr][Yy][_][Kk][Ee][Yy] ;

NOTNULL : [Nn][Oo][Tt] (WS)+ [Nn][Uu][Ll][Ll];

AND : [Aa][Nn][Dd];

OR : [Oo][Rr];

RELATIONAL : '=' | '>' | '<' | '>=' | '<=' | '!=' | BETWEEN | LIKE | IN ;

IDENTIFIER : [a-zA-Z_]+[a-zA-Z_0-9]* ;

logical : AND | OR ;

column : '*' | (WS)* column_name (WS)* (COMMA (WS)* column_name)*;

column_name : IDENTIFIER (DOT_IDENTIFIER)?;

table : IDENTIFIER (WS)* (COMMA (WS)* IDENTIFIER)*;

where_c :  WHERE (WS)+ condition;

DOT_IDENTIFIER : DOT IDENTIFIER;

s_condition : IDENTIFIER (DOT_IDENTIFIER)? (WS)* RELATIONAL (WS)* (IDENTIFIER| NUMBER | DATE | STRING);

condition : s_condition ((WS)+ logical (WS)+ s_condition)*;

values_c : (WS)* (NUMBER | STRING) (WS)* (COMMA (WS)* (NUMBER | STRING))*;

OPTIONS : PRIMARY | NOTNULL ;

VARTYPE : INT | VARCHAR | V_DATE;

ATTRIBUTE : IDENTIFIER (WS)+ VARTYPE ((WS)+ OPTIONS (WS)*)* ;

attributes : (WS)* ATTRIBUTE ((WS)* COMMA (WS)* ATTRIBUTE)* ;

describe_c : DESCRIBE (WS)+ IDENTIFIER (WS)* ';' ;