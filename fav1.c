#include<stdio.h>
#include<cs50.h>
void favorite() {
    string one = get_string("Your favorite color is:\n");
    printf("No way! My favorite color is %s, too!\n", one);
    string two = get_string("Your favorite movie is called:\n");
    printf("Really? You should know that The Princess Bride is better than %s!\n", two);
    string three = get_string("Your favorite animal is a/an:\n");
    printf("I forgot about %ss! Thanks for helping me remember that amazing animal!\n", three);
    string four = get_string("Your favorite dance move is known as:\n");
    printf("I think that %s is just okay. The moonwalk, on the other hand, is out of this world.\n", four);
    }
int main(void)
{
    favorite();
}