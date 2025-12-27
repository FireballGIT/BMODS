import java.util.ArrayList;
import java.util.Scanner;

public final class Tasker {
    public static ArrayList<String> tasks = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void addTasks(int numItems) {
        for (int i = 1; i <= numItems; i++) {
            System.out.print(i + ". Enter a task: ");
            String item = scanner.nextLine();
            tasks.add(item);
        }
    }

    public static void showItem(int index) {
        if (index >= 0 && index < tasks.size()) {
            System.out.println(tasks.get(index));
        } else {
            System.out.println("Error: Index " + index + " is out of range.");
        }
    }

    public static void removeItem(int index) {
        if (index >= 0 && index < tasks.size()) {
            String removed = tasks.remove(index);
            System.out.println("Removed item: '" + removed + "'");
        } else {
            System.out.println("Error: Index " + index + " is out of range. No item removed.");
        }
    }

    public static void showAll() {
        if (tasks.isEmpty()) {
            System.out.println("The task list is currently empty.");
        } else {
            System.out.println("Current Tasks:");
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    public static void clear() {
        tasks.clear();
    }
}
