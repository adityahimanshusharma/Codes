#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int find_min(unsigned int *adr, unsigned int size)
{
    int temp = *adr;
    for (int i = 0; i < size; i++)
    {
        if (*(adr + i) < temp)
            temp = *(adr + i);
    }
    return temp;
}

int main()
{
    srand(time(0));
    printf("Enter the size of the array: ");
    unsigned int x = 0;
    scanf("\n%d", &x);
    unsigned int numbers[x];
    for (int i = 0; i < x; i++)
    {
        numbers[i] = rand();
        printf("\t%d", numbers[i]);
    }
    printf("\n\nMinimum value: %d", find_min(numbers, x));
    printf("\n\n");
    return 0;
}