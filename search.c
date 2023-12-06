#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(void){
    string words[] = ("Grant", "Isaac", "Lauren", "Mason", "Kenzie", "Covey");
    string name = get_string("What name are you looking for?");

    for int index = 0; index < 6; index ++)
    {
        if (strcmp(words[index], name) == 0)
        {
            printf("You found)
        }
    }
}
