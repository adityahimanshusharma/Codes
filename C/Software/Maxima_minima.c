#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void find_max(unsigned int *addr,unsigned int *window_addr, unsigned int size)
{
    
}

void find_min(unsigned int *addr,unsigned int *window_addr, unsigned int size)
{
}

void arr_random_fill(int *addr, int x)
{
    // NOTE: This function requires the stdli.h & time.h libraries.

    srand(time(0));
    printf("\nFilling array.\n");
    for (unsigned int i = 0; i < x; i++)
    {
        *(addr + i) = rand();
    }
}

int main()
{
    srand(time(0));
    printf("Enter the size of the array: ");
    unsigned int size;
    scanf("%d", size);
    unsigned int samples[size];

    arr_fill(samples, size);

    printf("Define window size:");
    unsigned int window_size;
    scanf("%d", window_size);

    if (window_size < 3)
    {
        window_size = 3;
    }

    unsigned int middle_element = (window_size - 1) / 2; //to find the middle element of the window.

    unsigned int window[window_size];
    unsigned int *window_ptr_addr = window;

    find_max(samples, window_ptr_addr, size);
    find_min(samples, window_ptr_addr, size);

    printf("\n\n");
    return 0;
}