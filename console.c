#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LINES 1024
#define MAX_LINE_LEN 256

char console[MAX_LINES][MAX_LINE_LEN];
int consoleCount = 0;
int consoleExists = 0;

void getTimestamp(char* buffer, size_t size) {
    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    strftime(buffer, size, "%m/%d/%Y %H:%M", t);
}

void newConsole(const char* objectType) {
    char ts[20];
    getTimestamp(ts, sizeof(ts));
    if (strcmp(objectType, "console") == 0) {
        consoleCount = 0;
        consoleExists = 1;
        printf("[%s] Console object created/reset.\n", ts);
    } else if (strcmp(objectType, "log") == 0) {
        printf("[%s] Log object type not yet implemented.\n", ts);
    } else {
        printf("[%s] ERROR! Invalid object type.\n", ts);
    }
}

void logConsole(const char* msg) {
    char ts[20];
    getTimestamp(ts, sizeof(ts));
    if (consoleExists) {
        if (consoleCount < MAX_LINES) {
            snprintf(console[consoleCount], MAX_LINE_LEN, "[%s] %s", ts, msg);
            consoleCount++;
            printf("Logged: '[%s] %s'\n", ts, msg);
        }
    } else {
        printf("[%s] ERROR! No existing console object.\n", ts);
    }
}

// ... similar functions for terminate, clear, println, prntall, exportLog
