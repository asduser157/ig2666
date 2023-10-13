#include <cs50.h>
#include <stdio.h>

int main()
{
    int n1, n2, year;
    year = 0;
    n1 = 2;
    n2 = 3;
    int change = 0;
    do {
        printf("\nPlease enter the starting population size of llamas, ensuring your input is a number greater than 9 and less than 10,000: ");

        if (scanf ("%d", &n1) != 1)
        {
            printf("Please enter the starting population size of llamas, ensuring your input is a number greater than 9 and less than 10,000: ");
            while (getchar() != '\n');
        }
        else if (n1 < 9 || n1 > 10000)
        {
            printf("\nInput is out of range. ");
        }
        else if (n1 > 9 && n1 < 10000)
        {
            printf("\nOnce upon a time, there were %d llamas in Llamaland.\n", n1);
        }
    }
    while (n1 < 9 || n1 > 10000);

    do  {
        printf("\nPlease enter the ending population size of llamas, ensuring your input is a number greater than %d and less than or equal to 10,000: ", n1);

        if (scanf ("%d", &n2) != 1)
        {
            printf("\nPlease enter the ending population size of llamas, ensuring your input is a number greater than %d and less than 10,000: ", n1);
            while (getchar() != '\n');
        }
        else if (n2 < n1 || n2 > 10000)
        {
            printf("Input is out of range.\n");
        }
        else if (n2 > n1 && n2 < 10001){
        printf("\nA while later, the population had grown to %d llamas in Llamaland.\n", n2);
        int born = n1 / 3;
        int dead = n1 / 4;
        change = born - dead;
        }
    }
    while (n2 < n1);
    while (n1 < n2){
    
        n1 = n1 + change;
        year = year + 1;
    }
    printf("\nThat population growth took %d years!\n", year);


}