#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int decide = 0;
    double Fahrenheit;
    double Celsius;
    double Kelvin;
    printf("Welcome to the temperature converter engine!\n\n");
    Fahrenheit = get_double("Please type in a temperature in degrees Fahrenheit. \nNon-numerical characters (besides properly placed decimal points) will not be accepted. \n\nType it here: ");
    decide = get_int("_______________________________________________________________________________________\n\nWhich unit would you like to convert your temperature to?\n 1) Celsius \n 2) Kelvin \n");
    if (decide == 1)
    {
        Fahrenheit = Fahrenheit - 32;
        Celsius = (Fahrenheit * (5/9));
        printf("_______________________________________________________________________________________\n\nYour final temperature is: %lf °C \n", Celsius);
    }
    else if (decide == 2)
    {
        Celsius = ((5/9) * (Fahrenheit - 32));
        Kelvin = (Celsius + 273.15);
        printf("_______________________________________________________________________________________\n\nYour final temperature is: %lf K \n", Kelvin);
    }

}
