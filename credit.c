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
    beginning_numbers = card_long % (length - 2);
    if (beginning numbers = "








}