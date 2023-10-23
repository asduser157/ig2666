#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>
int main(void)
{
    char card_string[17];
    long card_number = get_long("Please enter a credit card number to test its validity.\n");
    sprintf(card_string, "%ld", card_number);
    int length = strlen(card_string);
    long card_long = atol(card_string);
    int b = 0;
    if (length == 16)
    {
        b = card_long / 100000000000000;
        int a1 = card_long / 10 % 10;
        int b1 = card_long / 1000 % 10;
        int c1 = card_long / 100000 % 10;
        int d1 = card_long / 10000000 % 10;
        int e1 = card_long / 1000000000 % 10;
        int f1 = card_long / 100000000000 % 10;
        int g1 = card_long / 10000000000000 % 10;
        int h1 = card_long / 1000000000000000 % 10;
        
        printf("%d, %d, %d, %d, %d, %d, %d, %d", a1, b1, c1, d1, e1, f1, g1, h1);
    }
    else if (length == 15)
    {
        b = card_long / 10000000000000;
    }
    else if (length == 13)
    {
        b = card_long / 100000000000;
    }
    if (b == 51 || b == 52 || b == 53 || b == 54 || b == 55)
    {
        printf("DISCOVER/MASTERCARD\n");
    }
    else if (b == 40 || b == 41 || b == 42 || b == 43 || b == 44 || b == 45 || b == 46 || b == 47 || b == 48 || b == 49)
    {
    printf("VISA\n");

    }
    else if ( b == 34 || b == 37)
    {
        printf("AMERICAN EXPRESS\n");
    }
    else
    {
        printf("***INVALID CREDIT CARD NUMBER***\n");
    }
}







