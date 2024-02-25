#include <stdio.h>
int main (void)
{
    int numbers[] = {3,5,2,8,5,7,0};
    int num;

    printf("Number to check on the list: ");
    scanf("%i", &num);

    for (int i=0; i<7; i++)
    {
        if (numbers[i] == num)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Number not found\n");
    return 1;
}