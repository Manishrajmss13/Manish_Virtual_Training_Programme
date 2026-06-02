#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <signal.h>

int N;

int isPrime(int num){
    if (num < 2) return 0;
    for (int i = 2; i * i <= num; i++){
        if (num % i == 0)
            return 0;
    }

    return 1;
}

void *threadA(void *arg){
    int count = 0;
    int num = 2;
    int sum = 0;

    while (count < N){
        if (isPrime(num)){
            sum += num;
            count++;
        }
        num++;
    }

    printf("\nSum of first %d prime numbers = %d\n", N, sum);

    pthread_exit(NULL);
}

void *threadB(void *arg){
    int time = 0;

    while (time < 100){
        printf("Thread 1 running every 2 seconds\n");
        sleep(2);
        time += 2;
    }

    pthread_exit(NULL);
}

void *threadC(void *arg){
    int time = 0;

    while (time < 100){
        printf("Thread 2 running every 3 seconds\n");
        sleep(3);
        time += 3;
    }

    pthread_exit(NULL);
}
void signalHandler(int sig)
{
    printf("\nSIGINT received. Program will not terminate.\n");
    fflush(stdout);
}
int main(){
    
    signal(SIGINT, signalHandler);
    pthread_t t1, t2, t3;

    printf("Enter N: ");
    scanf("%d", &N);

    pthread_create(&t1, NULL, threadA, NULL);
    pthread_create(&t2, NULL, threadB, NULL);
    pthread_create(&t3, NULL, threadC, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);
    return 0;
}