#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int decide = 0;
    printf("Welcome to the temperature converter engine!\n\n");
    double Fahrenheit = get_double("Please type in a temperature in degrees Fahrenheit. \nNon-numerical characters (besides properly placed decimal points) will not be accepted. \n\nType it here: ");
    decide = get_int("_______________________________________________________________________________________\n\nWhich unit would you like to convert your temperature to?\n 1) Celsius \n 2) Kelvin \n");
    double one = (Fahrenheit - 32);
    double two = (one * 5);
    double Celsius = (two / 9);
    double Kelvin = (Celsius + 273.15);
        if (decide == 1)
    {
        printf("_______________________________________________________________________________________\n\nYour final temperature is: %lf °C \n", Celsius);
    }
    else if (decide == 2)
    {
        printf("_______________________________________________________________________________________\n\nYour final temperature is: %lf K \n", Kelvin);
    }

}
