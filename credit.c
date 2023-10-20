#include <stdio.h>
#include <string.h>
#include <cs50.h>
int main(void)
{
    char card_string[17];
    long card_number = get_long("Please enter a credit card number to test its validity.");
    sprintf(card_string, "%d", card_number);
    



}