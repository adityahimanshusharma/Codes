/*This program generates an array of size n and rotates the no. of steps given by the user.*/

#include <stdio.h>

void rotate(int x[], __uint8_t steps, __uint8_t size)
{
    //int f = sizeof(x)/sizeof(x[0]); printf("\n%d",f);
    
    for (int i = 0; i < size; i++)
    {
        printf("\t%d", x[i]);
    }

    printf("\n\n");

    for (int i = 0; i < steps; i++)
    {
        long int temp = 0;
        temp = x[0];

        for (int j = 0; j < size; j++)
        {
            x[j] = x[j + 1];
        }
        x[size - 1] = temp;
    }

    for (int i = 0; i < size; i++)
    {
        printf("\t%d", x[i]);
    }
}

int main()
{
    int x, d;

    printf("Enter no of elements: ");
    scanf("\n%d", &d);

    int set[d];

    for (int i = 0; i < d; i++)
    {
        set[i] = i + 1;
    }

    printf("Enter no of Steps: ");
    scanf("\n%d", &x);

    d = sizeof(set);// / sizeof(set[0]);

    if (x > d)
        x = x % d;

    rotate(set, x, d);

    printf("\n\n");
    return 0;
}
