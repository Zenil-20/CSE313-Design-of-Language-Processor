%{
#include <stdio.h>
#include <string.h>

int lower=0, upper=0, digit=0, special=0;
%}
%%
[a-z]   { lower++; }
[A-Z]   { upper++; }
[0-9]   { digit++; }
[!@#$%^&*()] { special++; }
.|\n  
%%
int main() {
    yylex();
    if (lower > 0 && upper > 0 && digit > 0 && special > 0 && (lower + upper + digit + special) >= 9 && (lower + upper + digit + special) <= 15) {
        printf("Valid password\n");
    } else {
        printf("Invalid password\n");
    }
    return 0;
}
int yywrap() {
    return 1;
}
