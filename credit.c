#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>
int main(void)
{
    char card_string[17];
    long card_number = get_long("Please enter a credit card number to test its validity.\n");
    sprintf(card_string, "%ld", card_number);
    int length = strlen(card_string);
    long card_long = atol(card_string);
    int b = 0;
    int a1;
    int b1;
    int c1;
    int d1;
    int e1;
    int f1;
    int g1;
    int h1;
    int i1;
    int j1;
    int k1;
    int l1;
    int m1;
    int n1;
    int o1;
    int p1;
    int mult_a1;
    int mult_b1;
    int mult_c1;
    int mult_d1;
    int mult_e1;
    int mult_f1;
    int mult_g1;
    int mult_h1;
    int _a1;
    int _aa1;
    int _b1;
    int _bb1;
    int _c1;
    int _cc1;
    int _d1;
    int _dd1;
    int _e1;
    int _ee1;
    int _f1;
    int _ff1;
    int _g1;
    int _gg1;
    int _h1;
    int _hh1;
    int step1;
    int step2;
    int step3;
    if (length == 16)
    {
        b = card_long / 100000000000000;
        a1 = card_long / 10 % 10;
        b1 = card_long / 1000 % 10;
        c1 = card_long / 100000 % 10;
        d1 = card_long / 10000000 % 10;
        e1 = card_long / 1000000000 % 10;
        f1 = card_long / 100000000000 % 10;
        g1 = card_long / 10000000000000 % 10;
        h1 = card_long / 1 % 10;
        i1 = card_long / 100 % 10;
        j1 = card_long / 10000 % 10;
        k1 = card_long / 1000000 % 10;
        l1 = card_long / 100000000 % 10;
        m1 = card_long / 10000000000 % 10;
        n1 = card_long / 1000000000000 % 10;
        o1 = card_long / 100000000000000 % 10;
        p1 = card_long / 10000000000000000 % 10;
        mult_a1 = a1 * 2;
        mult_b1 = b1 * 2;
        mult_c1 = b1 * 2;
        mult_d1 = b1 * 2;
        mult_e1 = b1 * 2;
        mult_f1 = b1 * 2;
        mult_g1 = b1 * 2;
        mult_h1 = b1 * 2;
        _a1 = mult_a1 / 10;
        _aa1 = mult_a1 % 10;
        _b1 = mult_b1 / 10;
        _bb1 = mult_b1 % 10;
        _c1 = mult_c1 / 10;
        _cc1 = mult_c1 % 10;
        _d1 = mult_d1 / 10;
        _dd1 = mult_d1 % 10;
        _e1 = mult_e1 / 10;
        _ee1 = mult_e1 % 10;
        _f1 = mult_f1 / 10;
        _ff1 = mult_f1 % 10;
        _g1 = mult_g1 / 10;
        _gg1 = mult_g1 % 10;
        _h1 = mult_h1 / 10;
        _hh1 = mult_h1 % 10;
        step1 = _a1 + _aa1 + _b1 + _bb1 + _c1 + _cc1 + _d1 + _dd1 + _e1 + _ee1 + _f1 + _ff1 + g1 + _gg1 + _h1 + _hh1;
        step2 = step1 + i1 + j1 + k1 + l1 + m1 + n1 + o1 + p1;
        step3 = step2 % 10;
    }
    else if (length == 15)
    {
        b = card_long / 10000000000000;
    }
    else if (length == 13)
    {
        b = card_long / 100000000000;
    }
    if (b == 51 || b == 52 || b == 53 || b == 54 || b == 55)
    {
        printf("DISCOVER/MASTERCARD\n");
    }
    else if (b == 40 || b == 41 || b == 42 || b == 43 || b == 44 || b == 45 || b == 46 || b == 47 || b == 48 || b == 49)
    {
    printf("VISA\n");
    printf("%d\n", step2);
    printf("%d", step3);
        if (step3 == 0)
        {
            printf("***VALID CREDIT CARD NUMBER***\n");
        }
        else
        {
            printf("***INVALID CREDIT CARD NUMBER***");
        }

    }
    else if ( b == 34 || b == 37)
    {
        printf("AMERICAN EXPRESS\n");
    }
    else
    {
        printf("***INVALID CREDIT CARD NUMBER***\n");
    }
}







