#include <stdio.h>
#include <string.h>

int main (void)
{
    char* names[] = {"James", "Will", "Michael", "John"};
    char name [10];
    printf("Name to check in list: ");
    scanf("%s", &name);
    int length = sizeof(names)/sizeof(names[0]);

    for (int i=0; i<length;i++)
    {
        if (strcmp(names[i], name) == 0)
        {
            printf("Name found");
            return 0;
        }
    }
    printf("Name not found");
    return 1;
} 