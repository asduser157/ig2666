#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int decide = 0;
    double Fahrenheit = 0;
    double Celsius = 0;
    double Kelvin = 0;
    printf("Welcome to the temperature converter engine!\n\n");
    Fahrenheit = get_double("Please type in a temperature in degrees Fahrenheit. \nNon-numerical characters (besides properly placed decimal points) will not be accepted. \n\nType it here: ");
    decide = get_int("_______________________________________________________________________________________\n\nWhich unit would you like to convert your temperature to?\n 1) Celsius \n 2) Kelvin \n");
}
