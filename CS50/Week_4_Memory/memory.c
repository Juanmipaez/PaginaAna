#include <stdio.h>
#include <stdlib.h>
int main (void)
{
    int scores [3];
    int length = sizeof(scores)/sizeof(scores[0]);

    for (int i=0; i<length; i++)
    {
        printf("%i\n", scores[i]);
    }
}
