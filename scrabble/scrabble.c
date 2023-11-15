#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


    // rest of your code here

int compute1(string word1);
int compute2(string word2);


int main(void)
{
    // Get input words from both players
    int length = 0;
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");





    // TODO: Print the winner
}


// Score both words
int score1 = compute1(word1);
int score2 = compute2(word2);

int compute1(string word1)
{
    // TODO: Compute and return score for string
    for (int i = 0; i < strlen(word1); i++)
}

int compute2(string word2)
{
    // TODO: Compute and return score for string
    for (int i = 0; i < strlen(word2); i++)
}
