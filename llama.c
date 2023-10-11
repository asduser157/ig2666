#include <cs50.h>
#include <stdio.h>

int main(void)
{
    do {
        int n1 = get_int("Population Start Size: ");
        do {
            int n2 = get_int("Population End Size: ");
            printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
            int ans1 = n1 / 3;
            int ans2 = n1 / 4;
            int num = n2 - n1;
            int ans3 = ans1 - ans2;
            int final_ans = num / ans3;
            printf("That population growth took %i years.\n", final_ans);
            } while (n2 < n1);

        } while (n1 < 9);
}


