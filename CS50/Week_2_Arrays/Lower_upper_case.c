#include <stdio.h>
#include <string.h>

int main (void)
{

    int pregunta;
    printf("Convertir palabra a:\n1.Mayuscula \n2.Minuscula\n");
    do
    {
        printf("Ingrese opcion a elegir (1/2): ");
        scanf("%i", &pregunta);
    } 
    while (pregunta != 1 && pregunta != 2);
    
    char palabra [20];
    printf("Ingrese palabra: ");
    scanf("%s", &palabra);
    int length = strlen(palabra);

    if (pregunta == 1)
    {
        int i = 0;
        while (i<length)
        {
            if (palabra[i] >= 'a' && palabra[i <= 'z'])
            {
                printf("%c", palabra[i]-32);
            }
            else
            {
                printf("%c", palabra[i]);
            }
            i+=1;
        }
    }

    else if (pregunta == 2)
    {
        int i = 0;
        while (i<length)
        {
            if (palabra[i] >= 'A' && palabra[i] <= 'Z')
            {
                printf("%c", palabra[i]+32);
            }
            else
            {
                printf("%c", palabra[i]);
            }
            i+=1;
        }
    } 
}