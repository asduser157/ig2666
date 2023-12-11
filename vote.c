#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int age = get_string("How old are you?\n");
    int extra;
    if(age >= 0 && age < 18)
    {
        extra = 18 - age;
        printf("You are not eligible to vote. Please wait %i year(s)\n", extra);
    }
    else if(age == 18)
    {
        extra = 0;
        printf("Congratulations! For the first time in your life, you are eligible to vote!\n")
    }
    else if(age > 18 && age < 110)
    {
        printf(")
    }
}
