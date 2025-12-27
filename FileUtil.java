import java.io.*;
import java.nio.file.*;
import java.util.zip.*;

public final class FileUtil {

    public static boolean make(String path, String content) {
        try {
            File file = new File(path);
            if (file.exists()) return false;
            try (FileWriter writer = new FileWriter(file)) {
                writer.write(content);
            }
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public static String rename(String path, String newName) {
        File file = new File(path);
        if (!file.exists()) return "Error: Path does not exist.";
        File newFile = new File(file.getParent(), newName);
        if (file.renameTo(newFile)) return newFile.getAbsolutePath();
        return "Error: Rename failed.";
    }

    public static String renameExt(String path, String newExt) {
        File file = new File(path);
        if (!file.isFile()) return "Error: File does not exist.";
        if (!newExt.startsWith(".")) newExt = "." + newExt;
        String base = path.substring(0, path.lastIndexOf('.'));
        File newFile = new File(base + newExt);
        if (file.renameTo(newFile)) return newFile.getAbsolutePath();
        return "Error: Rename failed.";
    }

    public static boolean move(String src, String dst) {
        try {
            Files.move(Paths.get(src), Paths.get(dst), StandardCopyOption.REPLACE_EXISTING);
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public static boolean compress(String folderPath, String outputZip) {
        try {
            if (!outputZip.endsWith(".zip")) outputZip += ".zip";
            Path zipFile = Paths.get(outputZip);
            try (ZipOutputStream zos = new ZipOutputStream(Files.newOutputStream(zipFile))) {
                Files.walk(Paths.get(folderPath))
                     .filter(Files::isRegularFile)
                     .forEach(p -> {
                         ZipEntry entry = new ZipEntry(Paths.get(folderPath).relativize(p).toString());
                         try {
                             zos.putNextEntry(entry);
                             Files.copy(p, zos);
                             zos.closeEntry();
                         } catch (IOException e) { e.printStackTrace(); }
                     });
            }
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public static boolean extract(String zipPath, String outputDir) {
        try (ZipInputStream zis = new ZipInputStream(new FileInputStream(zipPath))) {
            ZipEntry entry;
            while ((entry = zis.getNextEntry()) != null) {
                File file = new File(outputDir, entry.getName());
                file.getParentFile().mkdirs();
                try (FileOutputStream fos = new FileOutputStream(file)) {
                    byte[] buffer = new byte[1024];
                    int len;
                    while ((len = zis.read(buffer)) > 0) {
                        fos.write(buffer, 0, len);
                    }
                }
            }
            return true;
        } catch (IOException e) {
            return false;
        }
    }
}
