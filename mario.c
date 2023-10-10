#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number;
    do
    {
        number = get_int("How many rows of hashtags?\n");
    }
    while(number < 1);

    for(int row = 0; row < 3; row ++)
    {
        for(int column = 0; column < 3; column++)
        {
        printf("#");
        }
        printf("\n");
    }
}