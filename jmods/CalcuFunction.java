import java.util.Scanner;

public final class CalcuFunction {

    private CalcuFunction() {}

    // ----------------
    // Core math
    // ----------------
    public static double add(double a, double b) { return a + b; }
    public static double sub(double a, double b) { return a - b; }
    public static double product(double a, double b) { return a * b; }
    public static double div(double a, double b) { return a / b; }
    public static double exp(double a, double b) { return Math.pow(a, b); }
    public static double floor(double a, double b) {
        return Math.floor(a / b);
    }

    // ----------------
    // CLI Calculator
    // ----------------
    public static void calculator() {
        Scanner sc = new Scanner(System.in);

        System.out.println("CalcuFunction Calculator");

        System.out.print("ENTER OPERATOR (+, -, *, /, //, ^): ");
        String op = sc.next();

        System.out.print("ENTER 1st NUMBER: ");
        double n1 = sc.nextDouble();

        System.out.print("ENTER 2nd NUMBER: ");
        double n2 = sc.nextDouble();

        switch (op) {
            case "+" -> System.out.println(add(n1, n2));
            case "-" -> System.out.println(sub(n1, n2));
            case "*" -> System.out.println(product(n1, n2));
            case "/" -> System.out.println(div(n1, n2));
            case "//" -> System.out.println(floor(n1, n2));
            case "^" -> System.out.println(exp(n1, n2));
            default -> System.out.println("ERROR! Invalid operator!");
        }
    }

  // ----------------
  // Extensions
  // ----------------

  public static Trig trig;
}
