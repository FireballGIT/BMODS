#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

int file_exists(const char *path) {
    struct stat buffer;
    return (stat(path, &buffer) == 0);
}

int make_file(const char *path, const char *content) {
    if (file_exists(path)) return 0;
    FILE *f = fopen(path, "w");
    if (!f) return 0;
    if (content) fprintf(f, "%s", content);
    fclose(f);
    return 1;
}

int rename_file(const char *path, const char *new_name) {
    if (!file_exists(path)) return 0;
    char new_path[512];
    snprintf(new_path, 512, "%s/%s", dirname(strdup(path)), new_name);
    return rename(path, new_path) == 0;
}

int rename_ext(const char *path, const char *new_ext) {
    if (!file_exists(path)) return 0;
    char new_path[512];
    const char *dot = strrchr(path, '.');
    int base_len = dot ? dot - path : strlen(path);
    snprintf(new_path, 512, "%.*s.%s", base_len, path, new_ext);
    return rename(path, new_path) == 0;
}

// Note: Move, compress, and extract would usually require platform-specific libraries in C.
// For simplicity, move can be implemented via rename:
int move_file(const char *src, const char *dst) {
    if (!file_exists(src)) return 0;
    return rename(src, dst) == 0;
}

// Full ZIP compress/extract is complicated in plain C; would need zlib. Skipping in basic version.
