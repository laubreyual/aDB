grammar Tuple;

tuple : data (',' data)*;

data : NUMBER | STRING ;

NUMBER : [0-9]*[.]?[0-9]+;

STRING :  ['] [A-Za-z0-9]* ['] | ["] [A-Za-z0-9]* ["]  ;
