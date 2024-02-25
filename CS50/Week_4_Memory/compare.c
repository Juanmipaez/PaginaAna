#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main (void)
{

    char i[10];
    printf ("i: ");
    scanf("%s", &i);

    char *t = malloc(strlen(i) + 1);
    if (t==NULL)
    {
        return 1;
    }
    strcpy(t,i);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("i: %s\n", i);
    printf("t: %s", t);

    free(t);
    return 0;

} 