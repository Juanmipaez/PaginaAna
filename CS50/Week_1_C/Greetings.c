#include <stdio.h>
int main(void) 
{
    char name[90];
    printf("Hey, what's your name?: ");
    scanf("%s", &name);
    printf("Hello, %s, nice to meet you!",name);
}