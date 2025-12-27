// ===============================
// CryptoHasher.h
// CMODS — One-Way Encoder
// ===============================

#ifndef CRYPTOHASHER_H
#define CRYPTOHASHER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define ALPHABET_68 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$"
#define SPECIAL_CHARS "!@#$%^&*"

char* encrypt(const char* text);

#endif
