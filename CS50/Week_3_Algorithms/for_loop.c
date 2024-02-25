#include <stdio.h>
#include <string.h>
int main (void)
{
    char name [20];
    printf("Word: ");
    scanf("%s", &name);
    int length = strlen(name);

    for (int i=0; i<length; i++)
    {
        printf("%c",name[i]);
        printf("\n");
    } 
}