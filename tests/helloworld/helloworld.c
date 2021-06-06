#include <stdio.h>

char message[] = "Hello World!";

void print_hello_world()
{
    int i;
    for(i=1;i<=10;i++)
    {
        printf("%d :%s\n", i, message);
    }
}