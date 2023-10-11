#include <cs50.h>
#include <stdio.h>

int main(void);


int safety_net(int n1, int n2, int ans1, int ans2, int num, int ans3, int final_ans)
{
    n1 = get_int("Population Start Size: ");
    if (n1 > 9)
    {
        if (n2 > n1)
        {
            printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
            ans1 = n1 / 3;
            ans2 = n1 / 4;
            num = n2 - n1;
            ans3 = ans1 - ans2;
            final_ans = num / ans3;
            printf("That population growth took %i years.\n", final_ans);
        }
    }
    else
    {
        safety_net(n1, n2, ans1, ans2, num, ans3, final_ans);
    }

return n1;
return n2;
return ans1;
return ans2;
return num;
return ans3;
return final_ans;
}

safety_net(n1, n2, ans1, ans2, num, ans3, final_ans);