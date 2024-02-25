#include <stdio.h>
#include <math.h>
int main (void) 

{
    float amount;
    int pennies;
    printf("Dollar amount: ");
    scanf("%f", &amount);
    pennies =round(amount * 100);
    printf("Amount in pennies: %i ", pennies);

}