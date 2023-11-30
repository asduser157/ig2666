#include <cs50.h>
#include <stdio.h>
void ask1()
{
    int snow = 0;
    int sun = 0;
    int rain = 0;
    int cloud = 0;
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
    {
        printf("Invalid number entered. Please try again.\n");
        ask1();
    }
}
void ask2()
{
    int question1 = get_int("Which best describes you? \n 1) I am generous, an when people see my true works they are amazed and thank me. \n 2) I try to be a positive person, and I appreciate the start of a new day.  \n 3) I am a creative person, and I strive to change so I can better help others. \n 4) I love helping others have fun, and I try to share the beauty in life with everyone.\n");
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
    {
        printf("Invalid number entered. Please try again.\n");
        ask2();
    }
}

void ask3()
{
    int question1 = get_int("Which best describes you? \n 1) I am generous, an when people see my true works they are amazed and thank me. \n 2) I try to be a positive person, and I appreciate the start of a new day.  \n 3) I am a creative person, and I strive to change so I can better help others. \n 4) I love helping others have fun, and I try to share the beauty in life with everyone.\n");
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
    {
        printf("Invalid number entered. Please try again.\n");
        ask2();
    }
}

int main(void)
{

    printf("Welcome to my quiz! \n");
    printf("Please type in the number associated with your answer. \n");
    ask1();
    ask2();

}
