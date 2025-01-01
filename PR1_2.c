#include<stdio.h>
#include<string.h>

void solve(char * arr, int n){
    if((n < 3 )|| (arr[n-1] != 'b' && arr[n-2] != 'b' && arr[0] != 'a')){
        printf("Invalid String\n");
        return;
    }

    for(int i=n-3; i >= 1; i--){
        if(arr[i] != 'a'){
            printf("Invalid String\n");
            return;
        }
    }

    printf("Valid String\n");
}

int main(){
    char * arr;
    scanf("%s", arr);

    int n = strlen(arr);

    // printf("%s", arr);

    solve(arr, n);

}
