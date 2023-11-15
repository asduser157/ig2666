#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


    // rest of your code here

int compute1(string word);
int compute2(string word);


int main(void)
{
    // Get input words from both players
    string word[2];
    int length = 0;
    int score1 = compute1(word);
    int score2 = compute2(word);
    word[0] = get_string("Player 1: ");
    word[1] = get_string("Player 2: ");

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


int compute1(string word)
{
    int score01 = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word1[i]))
        {
            score01 += points[word[i] - 'A'];
        }


        else if (islower(word[i]))
        {
            score01 += points[word[i] - 'a'];
        }
    }
}

int compute2(string word)
{
    int score02 = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            score02 += points[word[i] - 'A'];
        }

        else if (islower(word2[i]))
        {
            score02 += points[word[i] - 'a'];
        }
    }
}
