#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Hi there! What's your name?\n");
    printf("Nice to meet you, %s! \n", name);
}