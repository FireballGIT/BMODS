// ===============================
// CryptoHasher.js
// BMODS-JS — One-Way Encoder
// ===============================

const crypto = require('crypto');

const ALPHABET_68 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$";
const SPECIAL_CHARS = "!@#$%^&*";

function toBinary(text) {
  return [...text].map(c => c.charCodeAt(0).toString(2).padStart(8, '0')).join('');
}

function scrambleBits(bits, rand) {
  const arr = bits.split('');
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr.join('');
}

function chunk(bits, size) {
  const result = [];
  for (let i = 0; i < bits.length; i += size) {
    result.push(bits.slice(i, i + size));
  }
  return result;
}

function toBase68(bits) {
  while (bits.length % 6 !== 0) bits += '0';
  return chunk(bits, 6).map(c => ALPHABET_68[parseInt(c, 2) % 68]).join('');
}

function encrypt(text) {
  if (typeof text !== 'string' || text.length === 0) throw new Error("Input must be a non-empty string");

  // Step 1: string -> binary
  let binary = toBinary(text);

  // Step 2: entropy seed
  const hash = crypto.createHash('sha256').update(text).digest('hex');
  let seed = parseInt(hash.slice(0, 15), 16); // JS numbers can't hold full 256-bit int
  const rand = () => {
    seed = (seed * 9301 + 49297) % 233280;
    return seed / 233280;
  };

  // Step 3: scramble bits
  let scrambled = scrambleBits(binary, rand);

  // Step 4: convert to base68
  let encoded = toBase68(scrambled);

  // Step 5: inject one special character
  const special = SPECIAL_CHARS[Math.floor(rand() * SPECIAL_CHARS.length)];
  const pos = Math.floor(rand() * (encoded.length + 1));
  return encoded.slice(0, pos) + special + encoded.slice(pos);
}

module.exports = { encrypt };
