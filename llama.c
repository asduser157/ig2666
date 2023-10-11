#include <cs50.h>
#include <stdio.h>



int main(void)
{
    int n1 = get_int("Population Start Size: ");
    if (n1 > 9)
    {
        printf("Once upon a time, there were %i llamas in Llamaland.\n\n", n1);
        int n2 = get_int("Population End Size: ");
        if (n2 > n1)
        {
            printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
            int ans1 = n1/6;
            int ans2 = n1/11;
            int ans3 = ans1 - ans2;
            int final_ans = ans3*
            printf("That population growth took %i years.", final_ans);
            }
    }

}