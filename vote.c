#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int age = get_int("How old are you?\n");
    int extra = 0;
    if(age >= 0 && age < 18)
    {
        extra = 18 - age;
        printf("You are not eligible to vote. Please wait %i year(s).\n", extra);
    }
    else if(age == 18)
    {
        printf("Congratulations! You have officialy reached the age of being eligible to vote!\n");
    }
    else if(age > 18 && age < 111)
    {
        printf("You are eligible to vote!");
    }
    else if(age > 110)
    {
        printf("You are dead. Please enter in a younger age so you are still alive.");
    }
    else if(age < 0)
    {
        printf("You have not been born yet. Please enter in an older age so you are alive.");
    }
}
