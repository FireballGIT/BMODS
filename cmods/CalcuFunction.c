#include <stdio.h>
#include <math.h>

double add(double a, double b) { return a + b; }
double sub(double a, double b) { return a - b; }
double product(double a, double b) { return a * b; }
double divi(double a, double b) { return a / b; }
double expn(double a, double b) { return pow(a, b); }
double floor_div(double a, double b) {
    return floor(a / b);
}

void calculator() {
    char op[3];
    double n1, n2;

    printf("CalcuFunction Calculator\n");
    printf("ENTER OPERATOR (+, -, *, /, //, ^): ");
    scanf("%2s", op);

    printf("ENTER 1st NUMBER: ");
    scanf("%lf", &n1);

    printf("ENTER 2nd NUMBER: ");
    scanf("%lf", &n2);

    if (op[0] == '+' && op[1] == '\0')
        printf("%lf\n", add(n1, n2));
    else if (op[0] == '-' && op[1] == '\0')
        printf("%lf\n", sub(n1, n2));
    else if (op[0] == '*' && op[1] == '\0')
        printf("%lf\n", product(n1, n2));
    else if (op[0] == '/' && op[1] == '\0')
        printf("%lf\n", divi(n1, n2));
    else if (op[0] == '/' && op[1] == '/')
        printf("%lf\n", floor_div(n1, n2));
    else if (op[0] == '^' && op[1] == '\0')
        printf("%lf\n", expn(n1, n2));
    else
        printf("ERROR! Invalid operator!\n");
}
