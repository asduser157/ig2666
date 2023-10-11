#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n1 = get_int("Population Start Size: ");
    if (n1 > 9)
    {
        n2 = get_int("Population End Size: ");
        printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
        ans1 = n1 / 3;
        ans2 = n1 / 4;
        num = n2 - n1;
        ans3 = ans1 - ans2;
        final_ans = num / ans3;
        printf("That population growth took %i years.\n", final_ans);
    }
    else
    {

    }
}

