#include <cs50.h>
#include <stdio.h>

int main(void)


void
safety_net()
{
    int n1 = get_int("Population Start Size: ");
    if (n1 > 9)
    {
        ensure1();
    }
    else
    {
        safety_net();
    }
}

void
ensure1()
{
    printf("Once upon a time, there were %i llamas in Llamaland.\n\n", n1);
    int n2 = get_int("Population End Size: ");
}
void
ensure2()
{
    if (n2 > n1)
    {
        printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
        int ans1 = n1 / 3;
        int ans2 = n1 / 4;
        int num = n2 - n1;
        int ans3 = ans1 - ans2;
        int final_ans = num / ans3;
        printf("That population growth took %i years.\n", final_ans);
    }
    else
    {
        ensure1();
    }
}

safety_net();