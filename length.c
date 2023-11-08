#include<stdio.h>
#include<cs50.h>
#include<string.h>
int main(void)
{
    string name = get_string("What is your first name\n");
    int num = 0;
    while (name[num] != '\0')
    {
        num = num + 1;
    }
    printf("%i\n", num);
}