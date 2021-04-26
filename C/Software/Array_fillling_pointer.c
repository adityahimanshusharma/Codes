/*
This program generates random numbers and put them into array with the
size given by the user.
The element number, their address in the memory and the values holding
by the pointer are displayed
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    printf("Enter the size of the array:");
    unsigned int count = 0;
    scanf("%d", &count);
    unsigned int arr[count];
    unsigned int *addr = arr;
    printf("\nFilling the array:");
    for (unsigned int i = 0; i < count; i++)
    {
        *(addr + i) = rand();
    }

    printf("\n");
    printf("\nPrinting array with addresses:\n");
    printf("Element no.    ->    Address    ->    Value\n");
    for (unsigned int i = 0; i < count; i++)
    {
        printf("    %d    ->", i);
        printf("    %p    ->", &addr + i);
        printf("    %d", *(addr + i));
        printf("\n");
    }
    printf("\n\n");
    return 0;
}