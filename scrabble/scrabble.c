#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // rest of your code here

int compute(string words);
int main(void)
{
    // Get input words from both players

    string words[2];
    int length = 0;


    words[0] = get_string("\nPlayer 1: ");
    words[1] = get_string("Player 2: ");

    int score1 = compute(words[0]);
    int score2 = compute(words[1]);
    int diff = 0;

    if (score1 > score2)
    {
        diff = score1 - score2;
        printf("\nPLAYER 1: %i\nPLAYER 2: %i\n\nPlayer 1 is ahead by %i points!\n", score1, score2, diff);
    }
    else if (score1 < score2)
    {
        diff = score2 - score1;
        printf("\nPLAYER 1: %i\nPLAYER 2: %i\n\nPlayer 2 is ahead by %i points!\n", score1, score2, diff);
    }
    else if (score1 == score2)
    {
        diff = 0;
        printf("\nPLAYER 1: %i\nPLAYER 2: %i\n\nPlayer 1 and Player 2 are tied at %i points!\n", score1, score2, score2);
    }
}


int compute(string words)
{
    int score = 0;
    for (int i = 0; i < strlen(words); i++)
    {
        if (isupper(words[i]))
        {
            score += points[words[i] - 'A'];
        }


        else if (islower(words[i]))
        {
            score += points[words[i] - 'a'];
        }
    }
    return score;
}


