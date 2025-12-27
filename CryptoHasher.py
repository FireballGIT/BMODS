# ===============================
# 68Encryptor.py
# BAG Studios — One-Way Encoder
# ===============================

import random
import hashlib

# 64 URL-safe chars + 4 specials = 68
ALPHABET_68 = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$"
)

SPECIAL_CHARS = "!@#$%^&*"


def _to_binary(text: str) -> str:
    return "".join(f"{ord(c):08b}" for c in text)


def _scramble_bits(bits: str) -> str:
    bit_list = list(bits)
    random.shuffle(bit_list)
    return "".join(bit_list)


def _chunk(bits: str, size: int):
    return [bits[i:i + size] for i in range(0, len(bits), size)]


def _to_base68(bits: str) -> str:
    # pad to 6-bit alignment
    while len(bits) % 6 != 0:
        bits += "0"

    chunks = _chunk(bits, 6)
    return "".join(ALPHABET_68[int(chunk, 2) % 68] for chunk in chunks)


def encrypt(text: str) -> str:
    """
    One-way encoder.
    encrypt("hello") -> random-looking encoded string
    """

    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string.")

    # Step 1: string -> binary
    binary = _to_binary(text)

    # Step 2: entropy seed (content-based, not reversible)
    seed = int(hashlib.sha256(text.encode()).hexdigest(), 16)
    random.seed(seed)

    # Step 3: scramble bits
    scrambled = _scramble_bits(binary)

    # Step 4: convert to base68
    encoded = _to_base68(scrambled)

    # Step 5: inject one special character
    special = random.choice(SPECIAL_CHARS)
    pos = random.randint(0, len(encoded))
    final = encoded[:pos] + special + encoded[pos:]

    return final
