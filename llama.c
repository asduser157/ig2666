#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long n1 = get_long("Population Start Size:\n");
    while (n1 > 9)
    {
        printf("Once upon a time, there were %ld llamas on Lily Island.\n", n1);
        long n2 = get_long("Population End Size:\n");
        while (n2 > n1)
        {
            printf("A while later, the population had grown to %ld on)
        }

}