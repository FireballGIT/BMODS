#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASKS 1024
#define MAX_LEN 256

char tasks[MAX_TASKS][MAX_LEN];
int taskCount = 0;

void addTasks(int numItems) {
    char buffer[MAX_LEN];
    for (int i = 1; i <= numItems; i++) {
        printf("%d. Enter a task: ", i);
        fgets(buffer, MAX_LEN, stdin);
        buffer[strcspn(buffer, "\n")] = 0; // remove newline
        if (taskCount < MAX_TASKS) {
            strcpy(tasks[taskCount], buffer);
            taskCount++;
        } else {
            printf("Task list full!\n");
        }
    }
}

void showItem(int index) {
    if (index >= 0 && index < taskCount) {
        printf("%s\n", tasks[index]);
    } else {
        printf("Error: Index %d is out of range.\n", index);
    }
}

void removeItem(int index) {
    if (index >= 0 && index < taskCount) {
        printf("Removed item: '%s'\n", tasks[index]);
        for (int i = index; i < taskCount - 1; i++) {
            strcpy(tasks[i], tasks[i + 1]);
        }
        taskCount--;
    } else {
        printf("Error: Index %d is out of range. No item removed.\n", index);
    }
}

void showAll() {
    if (taskCount == 0) {
        printf("The task list is currently empty.\n");
    } else {
        printf("Current Tasks:\n");
        for (int i = 0; i < taskCount; i++) {
            printf("%d. %s\n", i + 1, tasks[i]);
        }
    }
}

void clearTasks() {
    taskCount = 0;
}
