%{
#include <stdio.h>
#include <stdlib.h>

int total_chars = 0;
int total_words = 0;
int total_lines = 0;
%}

%%

\n        { total_lines++; }
[a-zA-Z0-9]+ { 
             total_chars += yyleng;
             total_words++;
         }
[^a-zA-Z0-9 \t\n]+ { 
             total_chars += yyleng;
         }

%%

int yywrap(void) {
    return 1;
}

int main() {
    printf("Provide input:\n"); //ctrl+z to stop
    
    yylex();

    printf("\nTotal Characters: %d\n", total_chars);
    printf("Total Words: %d\n", total_words);
    printf("Total Lines: %d\n", total_lines);

    return 0;
}
