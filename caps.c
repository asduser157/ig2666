#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main(void)
{
    string input1 = get_string("Before: ");
    printf("After: ");
    for(int i = 0; i < strlen(input1); i ++)
    {
        if (input1[i] >= 'a' && input1[i] <= 'z')
        {
            printf("%c", input1[i] - 32);
        }
        else
        {
            printf("%c", input1[i]);
        }

    }
}