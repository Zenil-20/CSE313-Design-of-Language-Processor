%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *yyin;

int char_count = 0, word_count = 0, line_count = 1;
%}

%option noyywrap

KEYWORD      int|char|return|void|struct
IDENTIFIER   [a-zA-Z_][a-zA-Z0-9_]*
CONSTANT     [0-9]+
STRING       \"[^\"]*\"
PUNCTUATION  [(){};:,]
OPERATOR     [+\-*/=]

%%

{KEYWORD}    { printf("Keyword: %s\n", yytext); word_count++; char_count += yyleng; }
{IDENTIFIER} { printf("Identifier: %s\n", yytext); word_count++; char_count += yyleng; }
{CONSTANT}   { printf("Constant: %s\n", yytext); char_count += yyleng; }
{STRING}     { printf("String: %s\n", yytext); char_count += yyleng; }
{PUNCTUATION} { printf("Punctuation: %s\n", yytext); char_count++; }
{OPERATOR}   { printf("Operator: %s\n", yytext); char_count++; }
[\n]         { line_count++; char_count++; }
[ \t\r]+ 
.            { printf("Lexical Error: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("File opening failed");
            return EXIT_FAILURE;
        }
    }

    yylex();

    fclose(yyin);
    return 0;
}
