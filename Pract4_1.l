%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]+ {
    printf("%s\n", yytext);
}  
[^0-9] ;
%%

int yywrap(void) {
    return 1;
}

int main(void) {
    yylex();
    return 0;
}