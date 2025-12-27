// ===============================
// CryptoHasher.java
// JMODS — One-Way Encoder
// ===============================

package jmods;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

public class CryptoHasher {

    private static final String ALPHABET_68 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$";
    private static final String SPECIAL_CHARS = "!@#$%^&*";

    private static String toBinary(String text) {
        StringBuilder binary = new StringBuilder();
        for (char c : text.toCharArray()) {
            String bin = String.format("%8s", Integer.toBinaryString(c)).replace(' ', '0');
            binary.append(bin);
        }
        return binary.toString();
    }

    private static String scrambleBits(String bits, Random rand) {
        char[] arr = bits.toCharArray();
        for (int i = arr.length - 1; i > 0; i--) {
            int j = rand.nextInt(i + 1);
            char tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        return new String(arr);
    }

    private static String[] chunk(String bits, int size) {
        int len = bits.length();
        int count = (len + size - 1) / size;
        String[] chunks = new String[count];
        for (int i = 0; i < count; i++) {
            int start = i * size;
            int end = Math.min(start + size, len);
            chunks[i] = bits.substring(start, end);
        }
        return chunks;
    }

    private static String toBase68(String bits) {
        // pad to 6-bit alignment
        while (bits.length() % 6 != 0) {
            bits += "0";
        }

        StringBuilder encoded = new StringBuilder();
        for (String chunk : chunk(bits, 6)) {
            int val = Integer.parseInt(chunk, 2) % 68;
            encoded.append(ALPHABET_68.charAt(val));
        }
        return encoded.toString();
    }

    public static String encrypt(String text) throws NoSuchAlgorithmException {
        if (text == null || text.isEmpty()) {
            throw new IllegalArgumentException("Input must be a non-empty string.");
        }

        // Step 1: string -> binary
        String binary = toBinary(text);

        // Step 2: entropy seed
        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = sha256.digest(text.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes) {
            sb.append(String.format("%02x", b));
        }
        long seed = new java.math.BigInteger(sb.toString(), 16).longValue();
        Random rand = new Random(seed);

        // Step 3: scramble bits
        String scrambled = scrambleBits(binary, rand);

        // Step 4: convert to base68
        String encoded = toBase68(scrambled);

        // Step 5: inject one special character
        char special = SPECIAL_CHARS.charAt(rand.nextInt(SPECIAL_CHARS.length()));
        int pos = rand.nextInt(encoded.length() + 1);
        String finalStr = encoded.substring(0, pos) + special + encoded.substring(pos);

        return finalStr;
    }
}
