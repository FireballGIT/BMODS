// ===============================
// CryptoHasher.c
// CMODS — One-Way Encoder
// ===============================

#include "CryptoHasher.h"

// Simple pseudo-random generator for scrambling (not cryptographically secure)
static void scramble_bits(char* bits) {
    size_t len = strlen(bits);
    for (size_t i = len - 1; i > 0; i--) {
        size_t j = rand() % (i + 1);
        char tmp = bits[i];
        bits[i] = bits[j];
        bits[j] = tmp;
    }
}

static char* to_binary(const char* text) {
    size_t len = strlen(text);
    char* bin = malloc(len * 8 + 1);
    bin[0] = '\0';
    for (size_t i = 0; i < len; i++) {
        char buffer[9];
        for (int j = 7; j >= 0; j--) {
            buffer[7-j] = ((text[i] >> j) & 1) + '0';
        }
        buffer[8] = '\0';
        strcat(bin, buffer);
    }
    return bin;
}

static char* to_base68(const char* bits) {
    size_t len = strlen(bits);
    char* padded = malloc(len + 7);
    strcpy(padded, bits);
    while (strlen(padded) % 6 != 0) strcat(padded, "0");

    size_t chunks = strlen(padded) / 6;
    char* encoded = malloc(chunks + 2);
    for (size_t i = 0; i < chunks; i++) {
        char chunk[7];
        strncpy(chunk, padded + i*6, 6);
        chunk[6] = '\0';
        int val = (int)strtol(chunk, NULL, 2) % 68;
        encoded[i] = ALPHABET_68[val];
    }
    free(padded);
    encoded[chunks] = '\0';
    return encoded;
}

char* encrypt(const char* text) {
    if (!text || strlen(text) == 0) return NULL;

    srand((unsigned int)time(NULL));

    char* binary = to_binary(text);
    scramble_bits(binary);
    char* encoded = to_base68(binary);
    free(binary);

    size_t len = strlen(encoded);
    char* finalStr = malloc(len + 2);

    strcpy(finalStr, encoded);
    free(encoded);

    char special = SPECIAL_CHARS[rand() % strlen(SPECIAL_CHARS)];
    int pos = rand() % (len + 1);
    memmove(finalStr + pos + 1, finalStr + pos, len - pos + 1);
    finalStr[pos] = special;

    return finalStr;
}
