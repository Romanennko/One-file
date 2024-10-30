#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int computer_num = rand() % 100 + 1;
    int user_num = 0, count = 0;

    while (1) {
        printf("Try your luck [0-100]: ");
        if (scanf("%d", &user_num) != 1) {
            puts("UPS!!!");
            break;
        }
        if (computer_num == user_num) {
            printf("You win! You needed for this %d attempts", count);
            break;
        }
        else if (computer_num > user_num) {
            puts("Your number is lower");
        }
        else if (computer_num < user_num) {
            puts("Your number is highest");
        }
        count++;
    }
    return 0;
}
