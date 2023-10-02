#include <stdio.h>
#include <cs50.h>
int main(void)
{
    printf("Hi! I am Askbot, the amazing bot who asks you fun questions! Get ready to type in your answer to the question, and then press 'enter' to go to the next one!\n");
    string animal = get_string("What is your favorite animal?\n");
    printf("Nice! My favorite animal is a snow leopard, but I think that a(n) %s is cool too.\n", animal);
    string song_artist = get_string("Who is your favorite music artist?\n");
    string song_title = get_string("What is your favorite song by them?\n");
    printf("I actually don't like %s's song called '%s', but I do like 'Lily' by Alan Walker.\n", song_title, song_artist);
}