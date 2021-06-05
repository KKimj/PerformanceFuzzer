#include <stdio.h>

char message[] = "Hello World!";

int main()
{
    int i;
    for(i=1;i<=10;i++)
    {
        printf("%s", message);
        printf("\n");
    }
    return 0;
}