#include <stdio.h>
#include <unistd.h>

int N;

int isPrime(int num)
{
    if(num < 2)
        return 0;

    for(int i = 2; i * i <= num; i++)
    {
        if(num % i == 0)
            return 0;
    }

    return 1;
}

void functionA()
{
    int count = 0;
    int num = 2;
    int sum = 0;

    while(count < N)
    {
        if(isPrime(num))
        {
            sum += num;
            count++;
        }
        num++;
    }

    printf("Sum of first %d prime numbers = %d\n", N, sum);
}

void functionB()
{
    int time = 0;

    while(time < 10)
    {
        printf("Function B running every 2 seconds\n");
        sleep(2);
        time += 2;
    }
}

void functionC()
{
    int time = 0;

    while(time < 10)
    {
        printf("Function C running every 3 seconds\n");
        sleep(3);
        time += 3;
    }
}

int main()
{
    printf("Enter N: ");
    scanf("%d", &N);

    functionA();
    functionB();
    functionC();

    return 0;
}