#include<stdio.h>
#include<cs50.h>
void favorite() {
    string array1[4];
    string one = get_string("What is your favorite color?\n");
    printf("No way! My favorite color is %s, too!\n", one);
    string two = get_string("What is your favorite movie?\n");
    printf("Really? You should know that The Princess Bride is better than %s!\n", two);
    }
int main(void)
{
    favorite();
}