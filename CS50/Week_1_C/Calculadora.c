#include <stdio.h>
int main(void)
{
    int elección;
    float num1, num2, Rsuma, Rresta, Rmult, Rdiv;
    
    printf("1.Suma\n2.Resta\n.3.Multiplicación\n4.División\nIngresa número de la operación a realizar: ");
    scanf("%i", &elección);

    if (elección == 1)
    {
        printf("Ingrese primer número: ");
        scanf("%f", &num1);
        printf("Ingrese segundo número: ");
        scanf("%f", &num2);
        Rsuma = (num1+num2);
        printf("Resultado = %.2f", Rsuma);
    }

    else if (elección == 2)
    {
        printf("Ingrese primer número: ");
        scanf("%f", &num1);
        printf("Ingrese segundo número: ");
        scanf("%f", &num2);
        Rresta = (num1-num2);
        printf("Resultado = %.2f", Rresta);
    }

    else if (elección == 3)
    {
        printf("Ingrese primer número: ");
        scanf("%f", &num1);
        printf("Ingrese segundo número: ");
        scanf("%f", &num2);
        Rmult = (num1*num2);
        printf("Resultado = %.2f", Rmult);
    }

    else if (elección == 4)
    {
        printf("Ingrese primer número: ");
        scanf("%f", &num1);
        printf("Ingrese segundo número: ");
        scanf("%f", &num2);
        Rdiv = (num1/num2);
        printf("Resultado = %.3f", Rdiv);
    }

    else 
    {
        printf("Input no válido, intente de nuevo");
    }
}
