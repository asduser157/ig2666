#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n1 = get_int("Population Start Size: ");
    while (n1 > 9)
    {
        printf("Once upon a time, there were %ld llamas in Llamaland.\n\n", n1);
        int n2 = get_int("Population End Size: ");
    }
    if (n2 > n1)
    {
        printf("A while later, the population had grown to %ld llamas in Llamaland.\n\n", n2);
        int n3 = get_int("How many years did it take for the llama popluation to grow to %ld?", n2);

    }

}