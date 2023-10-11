#include <cs50.h>
#include <stdio.h>

int main()
{
    int n1, n2;
    do {
        printf("Please enter the starting population size of llamas, ensuring your input is a number greater than 9 and less than 10,000: ");

        if (scanf ("%d", &n1) != 1)
        {
            printf("Please enter the starting population size of llamas, ensuring your input is a number greater than 9 and less than 10,000: ");
            while (getchar() != '\n');
        }
        else if (n1 < 9 || n1 > 10000)
        {
            printf("Input is out of range. Please enter a number between 9 and 10,000: ");
        } while (n1 < 9 || n1 > 10000);
        }

    do  {
        printf("Please enter the ending population size of llamas, ensuring your input is a number greater than the previous number you entered and less than or equal to 10,000: ");

        if (scanf ("%d", &n2) != 1)
        {
            printf("Please enter the ending population size of llamas, ensuring your input is a number greater than the previous number you entered and less than 10,000: ");
            while (getchar() != '\n');
        }
        else if (n2 < n1 || n2 > 10000)
        {
            printf("Input is out of range. Please enter a number greater than the previous number you entered and less than 10,000: ");
        } while (n1 < 9 || n1 > 10000);
    }  return 0;
}
    printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
    int ans1 = n1 / 3;
    int ans2 = n1 / 4;
    int num = n2 - n1;
    int ans3 = ans1 - ans2;
    int final_ans = num / ans3;
    printf("That population growth took %i years.\n", final_ans);

#include <stdio.h>

int main() {
    int number;
    int min = 1; // Minimum allowed value
    int max = 100; // Maximum allowed value

    do {
        printf("Please enter an integer between %d and %d: ", min, max);

        // Read the integer input from the user
        if (scanf("%d", &number) != 1) {
            // Input is not a valid integer
            printf("Invalid input. Please enter a valid integer.\n");
            // Clear the input buffer
            while (getchar() != '\n');
        }
        else if (number < min || number > max) {
            // Input is outside the specified range
            printf("Input is out of range. Please enter a number between %d and %d.\n", min, max);
        }
    } while (number < min || number > max);

    printf("You entered a valid integer: %d\n", number);

    return 0;
}
