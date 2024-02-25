#include <stdio.h>
int main (void) 

{
    int h;
    do
    {
        printf("Height: ");
        scanf("%i", &h);
    }
    while (h<1);


    int num_spc = h;
    int c = (h-1);
    int b=0;
    int d=1;
    int z=1;
    for (int i=0; i<h; i++)
    {
        int b=(num_spc-c);
        while (b<=num_spc)
        {
            printf(" ");
            b+=1;
        }
        int e = (num_spc-d);
        while(e<num_spc)
        {
            printf("#");
            e+=1;
        }
        printf(" ");
        int j = (h-z);
        while (j<h)
        {
            printf("#");
            j+=1;
        }
    printf("\n\n");  
    z+=1;    
    c-=1;
    d+=1;
    }
}
