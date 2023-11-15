#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // rest of your code here

int compute(string input_);


int main(void)
{
    // Get input words from both players
    string input_[2];
    int length = 0;
    input_[0] = get_string("Player 1: ");
    input_[1] = get_string("Player 2: ");
    int score1 = compute(input_[0]);
    int score2 = compute(input_[1]);

    if (score1 > score2)
    {
        printf("Player 1 is ahead with %i points!\n", score1);
    }
    else if (score1 < score2)
    {
        printf("Player 2 is ahead with %i points!\n", score2);
    }
    else if (score1 == score2)
    {
        printf("Player 1 is tied for %i points with Player 2!\n", score1);
    }
}


int compute(string input_)
{
    int score = 0;
    for (int i = 0; i < strlen(input_); i++)
    {
        if (isupper(input_[i]))
        {
            score += points[input_[i] - 'A'];
        }


        else if (islower(input_[i]))
        {
            score += points[input_[i] - 'a'];
        }
    }
    return score;
}


