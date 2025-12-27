import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public final class Console {

    public static ArrayList<String> console = new ArrayList<>();
    public static boolean consoleExists = false;

    public static String getTimestamp() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm");
        return LocalDateTime.now().format(formatter);
    }

    public static void newConsole(String objectType) {
        switch (objectType) {
            case "console":
                console.clear();
                consoleExists = true;
                System.out.println("[" + getTimestamp() + "] Console object created/reset.");
                break;
            case "log":
                System.out.println("[" + getTimestamp() + "] Log object type not yet implemented.");
                break;
            default:
                System.out.println("[" + getTimestamp() + "] ERROR! Invalid object type.");
        }
    }

    public static void log(String msg) {
        if (consoleExists) {
            String timestampedMsg = "[" + getTimestamp() + "] " + msg;
            console.add(timestampedMsg);
            System.out.println("Logged: '" + timestampedMsg + "'");
        } else {
            System.out.println("[" + getTimestamp() + "] ERROR! No existing console object.");
        }
    }

    public static void terminate(int index) {
        if (consoleExists) {
            try {
                String removed = console.remove(index);
                log("Terminated line " + index + ": '" + removed + "'");
            } catch (IndexOutOfBoundsException e) {
                log("ERROR! Index " + index + " is out of range.");
            }
        } else {
            System.out.println("[" + getTimestamp() + "] ERROR! No existing console object.");
        }
    }

    public static void clear() {
        if (consoleExists) {
            console.clear();
            log("Console cleared.");
        } else {
            System.out.println("[" + getTimestamp() + "] ERROR! No existing console object.");
        }
    }

    public static void println(int index) {
        if (consoleExists) {
            try {
                System.out.println(console.get(index));
            } catch (IndexOutOfBoundsException e) {
                System.out.println("[" + getTimestamp() + "] ERROR! Index " + index + " is out of range.");
            }
        } else {
            System.out.println("[" + getTimestamp() + "] ERROR! No existing console object.");
        }
    }

    public static void prntall() {
        if (consoleExists) {
            if (console.isEmpty()) {
                log("Console is empty.");
                return;
            }
            System.out.println("--- Console Start ---");
            for (String s : console) {
                System.out.println(s);
            }
            System.out.println("--- Console End ---");
        } else {
            System.out.println("[" + getTimestamp() + "] ERROR! No existing console object.");
        }
    }

    public static void exportLog(String filename, String directory) {
        if (filename == null || filename.isEmpty()) filename = "output_log";
        if (directory == null || directory.isEmpty()) directory = ".";

        if (consoleExists && !console.isEmpty()) {
            File dir = new File(directory);
            if (!dir.exists()) dir.mkdirs();

            File file = new File(dir, filename + ".bmlog");
            try (FileWriter writer = new FileWriter(file)) {
                for (String line : console) {
                    writer.write(line + "\n");
                }
                log("Successfully exported console to '" + file.getAbsolutePath() + "'.");
            } catch (IOException e) {
                log("ERROR! Could not write to file " + file.getAbsolutePath() + ": " + e.getMessage());
            }
        } else if (consoleExists) {
            log("Console is empty; nothing to export.");
        } else {
            log("ERROR! No existing console object to export.");
        }
    }
}
