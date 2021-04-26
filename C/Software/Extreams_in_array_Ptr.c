#include <stdio.h>
//#include <math.h>

void find_max(int *addr, unsigned int size)
{

}

void find_min(int *addr, unsigned int size)
{

}

void sort(int *addr, unsigned int size)
{
    
}

int main()
{
    printf("Enter the size of the array: ");
    int x;
    scanf("%d", x);
    unsigned int samples[x];
    int *adr = samples[x];
    printf("\nFilling array.\n");
    for (unsigned int i = 0; i < x; i++)
    {
        samples[i] = rand();
        printf("\t%d", samples[i]);
    }

    find_max(adr, x);
    find_min(adr, x);
    return 0;
}