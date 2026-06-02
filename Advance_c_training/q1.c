#include<stdio.h>
#include<string.h>

struct Day{
    char day[10];
    char task[3][100];
};

int main(){
    struct Day week[7] = {
        {"Monday"},
        {"Tuesday"},
        {"Wednesday"},
        {"Thursday"},
        {"Friday"},
        {"Saturday"},
        {"Sunday"}
    };

    int d,t;

    while(1){
        printf("\n===== Days of the Week =====\n");
        for(int i=0;i<7;i++){
            printf("%d. %s\n",i+1,week[i].day);
        }

        printf("\nEnter day number (1-7) or 0 to Exit: ");
        scanf("%d", &d);
        getchar();

        if(d==0) break;
        if(d<1 || d>7){
            printf("Invalid day number!\n");
            continue;
        }

        printf("Enter number of tasks (Max 3): ");
        scanf("%d", &t);
        getchar();

        if(t>3) t=3;

        for(int i = 0; i < t; i++){
            printf("Enter Task %d: ", i + 1);
            fgets(week[d-1].task[i], 100, stdin);
            week[d-1].task[i][strcspn(week[d-1].task[i], "\n")] = '\0';
        }
    }

    printf("\n===== WEEKLY CALENDAR =====\n");
    for(int i = 0; i < 7; i++){
        printf("\n%s\n", week[i].day);
        for(int j = 0; j < 3; j++){
            if(strlen(week[i].task[j]) > 0){
                printf("- %s\n", week[i].task[j]);
            }
        }
    }
    return 0;
}