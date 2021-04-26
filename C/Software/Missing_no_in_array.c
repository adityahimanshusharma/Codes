#include <stdio.h>

unsigned int find_min(int *adr, unsigned int size)
{
    //int temp = *adr;
    for (int i = 0; i < size; i++)
    {
        if (*(adr + i) < temp)
            temp = *(adr + i);
    }

    return temp;
}

int main()
{
    printf("Enter the size of the array:");
    int x = 0;
    scanf("\n%d", x);
    unsigned int numbers[x];
    for (int i = 0; i < x; i++)
    {
        numbers[i] = rand();
        printf("\t%d", numbers[i]);
    }

    find_min(&numbers[],x);
    return 0;
}