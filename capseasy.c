#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    string input1 = get_string("Before: ");
    printf("After: ");
    for (int i = 0; i < strlen(input1); i++)
    {
        printf("%c", toupper(input1[i]));
    }
}