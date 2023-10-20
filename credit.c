#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>
int main(void)
{
    char card_string[17];
    long card_number = get_long("Please enter a credit card number to test its validity.");
    sprintf(card_string, "%d", card_number);
    int length = strlen(card_string);
    long card_long = atol(card_string);
    b = card_long % (length - 2);
    if (b = "51" || b = "52" || b = "53" || b = "54" || b = "55")
    {
        printf("DISCOVER/MASTERCARD");
    }
    else if (b = "40" || b = "41" || b = "42" || b = "43" || b = "44" || b = "45" || b = "46" || b = "47" || b = "48" || b = "49")
    {
        printf("VISA");
    }
    else if ( b = "34" || b = "37")
    {
        printf("AMERICAN EXPRESS");
    }






}