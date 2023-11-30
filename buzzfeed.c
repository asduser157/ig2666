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
        printf("Invalid number entered. Please try again.\n\n");
        ask1();
    }
    int question2 = get_int("Which best describes you? \n 1) I am generous, an when people see my true works they are amazed and thank me. \n 2) I try to be a positive person, and I appreciate the start of a new day.  \n 3) I am a creative person, and I strive to change so I can better help others. \n 4) I love helping others have fun, and I try to share the beauty in life with everyone.\n");
    if(question2 == 1)
    {
        rain++;
    }
    else if(question2 == 2)
    {
        sun++;
    }
    else if(question2 == 3)
    {
        cloud++;
    }
    else if(question2 == 4)
    {
        snow++;
    }
    else
    {
        printf("Invalid number entered. Please try again.\n\n");
        ask1();
    }
    int question3 = get_int("Which state would you prefer to live in? \n 1) Louisville, KY \n 2) Sacramento, CA \n 3) Seattle, WA \n 4) Buffalo, NY \n");
    if(question3 == 1)
    {
        rain++;
    }
    else if(question3 == 2)
    {
        sun++;
    }
    else if(question3 == 3)
    {
        cloud++;
    }
    else if(question3 == 4)
    {
        snow++;
    }
    else
    {
        printf("Invalid number entered. Please try again.\n\n");
        ask1();
    }
    int question3 = get_int("Which shape do you like the most? \n 1) Triangle \n 2) Circle \n 3) Rectangle \n 4) Hexagon \n");
    if(question4 == 1)
    {
        rain++;
    }
    else if(question4 == 2)
    {
        sun++;
    }
    else if(question4 == 3)
    {
        cloud++;
    }
    else if(question4 == 4)
    {
        snow++;
    }
    else
    {
        printf("Invalid number entered. Please try again.\n\n");
        ask1();
    }
    int question5 = get_int("Which state would you prefer to live in? \n 1) Louisville, KY \n 2) Sacramento, CA \n 3) Seattle, WA \n 4) Buffalo, NY \n");
    if(question5 == 1)
    {
        rain++;
    }
    else if(question5 == 2)
    {
        sun++;
    }
    else if(question5 == 3)
    {
        cloud++;
    }
    else if(question5 == 4)
    {
        snow++;
    }
    else
    {
        printf("Invalid number entered. Please try again.\n\n");
        ask1();
    }
}

int main(void)
{

    printf("Welcome to my quiz! \n");
    printf("Please type in the number associated with your answer. \n");
    ask1();

}
