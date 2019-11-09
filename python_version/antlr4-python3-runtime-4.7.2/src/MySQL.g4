grammar MySQL;

s : select_c | delete_c | insert_c | create_c | describe_c | show_c | drop_c | exit_c;

select_c : SELECT (WS)+ column (WS)+ FROM (WS)+ table (WS)* (where_c)? (WS)* ';' ;

delete_c : DELETE (WS)+ FROM (WS)+ table (WS)* (where_c)? (WS)* ';' ;

insert_c : INSERT (WS)+ table ((WS)* PL column PR)? (WS)+ VALUES (WS)* PL values_c PR ';' (WS)* ;

create_c : CREATE (WS)+ table (WS)* PL (WS)* attributes (WS)* (fkey_cons)? PR (WS)*';' ;

SHOW : [Ss][Hh][Oo][Ww] (WS)* [Tt][Aa][Bb][Ll][Ee][Ss] ;

show_c : SHOW (WS)* ';' ;

DROP : [Dd][Rr][Oo][Pp] (WS)* [Tt][Aa][Bb][Ll][Ee] ;

drop_c : DROP (WS)* table (WS)* ';' ;

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

FLOAT : [Ff][Ll][Oo][Aa][Tt] (WS)* PL (WS)* [0-9] COMMA [0-4] (WS)* PR;

V_DATE : [Dd][Aa][Tt][Ee];

PRIMARY : [Pp][Rr][Ii][Mm][Aa][Rr][Yy][_][Kk][Ee][Yy] ;

NOTNULL : [Nn][Oo][Tt] (WS)+ [Nn][Uu][Ll][Ll];

AND : [Aa][Nn][Dd];

OR : [Oo][Rr];

RELATIONAL : '=' | '>' | '<' | '>=' | '<=' | '!=' | BETWEEN | LIKE | IN ;

REFERENCES : [Rr][Ee][Ff][Ee][Rr][Ee][Nn][Cc][Ee][Ss];

IDENTIFIER : [a-zA-Z_]+[a-zA-Z_0-9]* ;

logical : AND | OR ;

column : '*' | (WS)* column_name (WS)* (COMMA (WS)* column_name)*;

column_name : IDENTIFIER (DOT_IDENTIFIER)?;

table : IDENTIFIER (WS)* (COMMA (WS)* IDENTIFIER)*;

where_c :  WHERE (WS)+ condition;

DOT_IDENTIFIER : DOT IDENTIFIER;

s_condition : IDENTIFIER (DOT_IDENTIFIER)? (WS)* RELATIONAL (WS)* (IDENTIFIER| NUMBER | DATE | STRING);

condition : s_condition ((WS)+ logical (WS)+ s_condition)*;

value: (NUMBER | STRING | DATE);

values_c : (WS)* (value) (WS)* (COMMA (WS)* (value))*;

OPTIONS : PRIMARY | NOTNULL ;

VARTYPE : FLOAT | VARCHAR | V_DATE;

ATTRIBUTE : IDENTIFIER (WS)+ VARTYPE ((WS)+ OPTIONS (WS)*)* ;

attributes : (WS)* ATTRIBUTE ((WS)* COMMA (WS)* ATTRIBUTE)* ;

describe_c : DESCRIBE (WS)+ IDENTIFIER (WS)* ';' ;

FOREIGN_KEY : [Ff][Oo][Rr][Ee][Ii][Gg][Nn] (WS)+ [Kk][Ee][Yy] ;

fkey_cons : COMMA (WS)* FOREIGN_KEY (WS)* PL (WS)* IDENTIFIER (WS)* PR (WS)+ REFERENCES (WS)+ IDENTIFIER (WS)* PL (WS)* IDENTIFIER (WS)* PR;



