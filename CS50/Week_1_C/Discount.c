#include <stdio.h>

// Se declara la función, especificando el tipo de dato.
float discount (float price, float per_off)
{
    return price * ((1)-(per_off/100));
}

int main (void)
{
    float regular_p, sale, substracted;
    int per_off;
    printf("Regular price: ");
    scanf("%f", &regular_p);
    printf("Percentage off: ");
    scanf("%i", &per_off);
    sale = discount(regular_p, per_off);
    substracted = (regular_p - sale);
    printf("Sale price: %.2f (-%.2f)", sale, substracted);
}

