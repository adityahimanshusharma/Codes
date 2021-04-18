//This is an implementation of Arrays and size of function.

#include <stdio.h>

int main()
{
    int g[4];
    int i = 0;

    printf("Enter No: ");

    for (i = 0; i < sizeof(g) / sizeof(i); i++)
    {
        scanf("\n%d", &g[i]);
    }

    for (i = 0; i < sizeof(g) / sizeof(i); i++)
    {
        printf("\n%d", g[i]);
        printf("\n%ld", &g[i]);
    }

    printf("\n%d", i);
    printf("\n%d", &i);
    return 0;
}