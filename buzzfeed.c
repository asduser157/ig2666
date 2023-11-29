#include <cs50.h>
#include <stdio.h>
int snow = 0;
int sun = 0;
int rain = 0;
int cloud = 0;
int main(void)
{

    printf("Welcome to my quiz! \n");
    printf("Please type in the number associated with your answer. \n");

    int question1 = get_int("What is your favorite season? \n 1) Spring \n 2) Summer \n 3) Fall \n 4) Winter\n");
    if(question1 == 1)
    {
        rain++;
    }
    else if(question1 == 2)
    {
        sun++;
    }
    else if(question1 == 3)
    {
        cloud++;
    }
    else if(question1 == 4)
    {
        snow++;
    }
    else

}
