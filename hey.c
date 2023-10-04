#include <stdio.h>
#include <cs50.h>
int main(void)
{
    char c = get_char("Do you agree to us collecting your data and selling it to the North Korean government?\n");

    if (c == 'Y' || c == 'y')
    {
        printf("You have agreed.\n");
    }
    if (c == 'n' || c == 'N')
    {
        printf("You have not agreed, so we will not only collect your data, but your family's data too. It's too bad you didn't agree the first time!\n");
    }
}