#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z;
A = 1;
B = 3;
C = 3;
D = 2;
E = 1;
F = 4;
G = 2;
H = 4;
I = 1;
J = 8;
K = 5;
L = 1;
M = 3;
N = 1;
O = 1;
P = 3;
Q = 10;
R = 1;
S = 1;
T = 1;
U = 1;
V = 4;
W = 4;
X = 8;
Y = 4;
Z = 10;
char* getCharacters1(char* word1)
{
    
}
char* getCharacters2(char* word2)
{
    // function implementation here
}


    // rest of your code here

int compute(string word);


int main(void)
{
    // Get input words from both players
    char* word1 = get_string("Player 1: ");
    char* word2 = get_string("Player 2: ");
    char* character1 = getCharacters(word1);
    char* character2 = getCharacters(word2);
    for (int i = 0; i < strlen(word1); i++)
    {
        word1 = toupper(word1[i]);
        printf("%s", word1)
    }
    for (int i = 0; str[i] != '\0'; i++)
    {
        word2 = toupper(word2[i]);
        printf("%s", word2)
    }

    // Score both words
    int score1 = compute(word1);
    int score2 = compute(word2);

    // TODO: Print the winner
}

int compute(string word)
{
    // TODO: Compute and return score for string
}
