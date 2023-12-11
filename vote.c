#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
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
        char vote = get_char("Who do you want to vote for?\n  a) Mickey Mouse \n  b) Winnie the Pooh \n  c) Bugs Bunny \n  d) Scooby Doo \n  e) Ozzy Osbourne \n");
    }
    else if(age > 18 && age < 111 && age != 35)
    {
        printf("You are eligible to vote!");
        char vote = get_char("Who do you want to vote for?\n  a) Mickey Mouse \n  b) Winnie the Pooh \n  c) Bugs Bunny \n  d) Scooby Doo \n  e) Ozzy Osbourne \n");
    }
    else if(age == 35)
    {
        printf("You are not only eligible to vote, but you are now eligible to run for president!*\n\n*You must be a natural born U.S. citizen and have been a resident of the U.S. for at least 14 years.\n");
        char vote = get_char("Who do you want to vote for?\n  a) Mickey Mouse \n  b) Winnie the Pooh \n  c) Bugs Bunny \n  d) Scooby Doo \n  e) Ozzy Osbourne \n  f) Yourself \n");
        if(vote == 'a')
        {
            printf("Eek! Walt Disney was afraid of mice. Hold on a second to see if Mickey wins!\n");
        }
        if(vote == 'b')
        {
            printf("Winnie the Pooh is the patron saint of teddy bears! Let's see if Winnie wins!\n");
        }
        if(vote == 'c')
        {
            printf("The actor for Bugs Bunny was allergic to carrots! Wait to see if Bugs wins!\n");
        }
        if(vote == 'd')
        {
            printf("Scooby-Doo's real name is Scoobert. Let's hold on and see if Scooby-Doo wins!\n");
        }
        if(vote == 'e')
        {
            printf("You're going off the rails on a crazy train! Stay to find out if Ozzy wins!\n");
        }
        if(vote == 'f')
        {
            printf("You are in the mix of candidates! Let's wait for a bit and see if you win!\n");
        }
        else
        {
            printf("Uh-oh! Your vote was not valid. I guess Ozzy Osbourne got an extra unexpected vote!\n");
        }
        char *array1[6] = {"Mickey Mouse!", "Winnie the Pooh!", "Bugs Bunny!", "Scooby-Doo!", "Ozzy Osbourne!", "You!"};
        int randomIndex = rand() % 6;
        char *randomElement = array1[randomIndex];
        printf("The winner is............................. ");
        printf("%c", randomElement);
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
