#include <stdio.h>

// char message[] = "Hello World!";
extern char message[];
extern void print_hello_world();

int main()
{
    int i;
    for(i=1;i<=10;i++)
    {
        printf("%d :%s", i, message);
        printf("\n");
        print_hello_world();
    }
    return 0;
}