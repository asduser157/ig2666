#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int A = 1;
int B = 3;
int C = 3;
int D = 2;
int E = 1;
int F = 4;
int G = 2;
int H = 4;
int I = 1;
int J = 8;
int K = 5;
int L = 1;
int M = 3;
int N = 1;
int O = 1;
int P = 3;
int Q = 10;
int R = 1;
int S = 1;
int T = 1;
int U = 1;
int V = 4;
int W = 4;
int X = 8;
int Y = 4;
int Z = 10;


    // rest of your code here

int compute(string word);


int main(void)
{
    // Get input words from both players
    int length = 0;
    int length1 = 0;
    string word1 = get_string("Player 1: ");
    length = strlen(word1);
    for (int i = 0; i < length; i++)
    {
        printf("%c", toupper(word1[i]));
    }
        printf("\n");
    for (int i = 0; i < length; i++)
    {
        int length1 = 0;
        length1 = length1 + 1;

        printf("%c", str[]);

    }


    // h

    return 0;



    // TODO: Print the winner
}


// Score both words
    //int score1 = compute(word1);
    //int score2 = compute(word2);

//int compute(string word)
//{
    // TODO: Compute and return score for string
  //}
