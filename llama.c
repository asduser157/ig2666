#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("Population Start Size: ");
    int n2 = get_int("Population End Size: ");
    printf("A while later, the population had grown to %i llamas in Llamaland.\n\n", n2);
    int ans1 = n1 / 3;
    int ans2 = n1 / 4;
    int num = n2 - n1;
    int ans3 = ans1 - ans2;
    int final_ans = num / ans3;
    printf("That population growth took %i years.\n", final_ans);
}
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
