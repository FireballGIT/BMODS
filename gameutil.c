#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_PLAYERS 1024
#define MAX_DICE 1024

int players[MAX_PLAYERS];
int maxHP[MAX_PLAYERS];
int playerCount = 0;

int dice[MAX_DICE];
int diceCount = 0;

// ===============================
// OBJECT CREATION
// ===============================
int newPlayer(int startingHP) {
    if (startingHP <= 0) return -1;
    int id = playerCount++;
    players[id] = startingHP;
    maxHP[id] = startingHP;
    return id;
}

int newDie(int sides) {
    if (sides < 2) return -1;
    int id = diceCount++;
    dice[id] = sides;
    return id;
}

// ===============================
// PLAYER HP SYSTEM
// ===============================
int setMaxHP(int playerId, int max_hp) {
    if (playerId < 0 || playerId >= playerCount) return -1;
    if (max_hp <= 0) return -1;
    maxHP[playerId] = max_hp;
    if (players[playerId] > max_hp) players[playerId] = max_hp;
    return 0;
}

int atk(int damage, int playerId) {
    if (playerId < 0 || playerId >= playerCount) return -1;
    if (damage < 0) return -1;
    players[playerId] -= damage;
    if (players[playerId] < 0) players[playerId] = 0;
    return players[playerId];
}

int heal(int amount, int playerId) {
    if (playerId < 0 || playerId >= playerCount) return -1;
    if (amount < 0) return -1;
    players[playerId] += amount;
    if (players[playerId] > maxHP[playerId]) players[playerId] = maxHP[playerId];
    return players[playerId];
}

int getHP(int playerId) {
    if (playerId < 0 || playerId >= playerCount) return -1;
    return players[playerId];
}

// ===============================
// DICE SYSTEM
// ===============================
int rollDie(int dieId) {
    if (dieId < 0 || dieId >= diceCount) return -1;
    return (rand() % dice[dieId]) + 1;
}

// ===============================
// DELETE SYSTEM
// ===============================
int deletePlayer(int playerId) {
    if (playerId < 0 || playerId >= playerCount) return -1;
    for (int i = playerId; i < playerCount - 1; i++) {
        players[i] = players[i + 1];
        maxHP[i] = maxHP[i + 1];
    }
    playerCount--;
    return 0;
}

int deleteDie(int dieId) {
    if (dieId < 0 || dieId >= diceCount) return -1;
    for (int i = dieId; i < diceCount - 1; i++) {
        dice[i] = dice[i + 1];
    }
    diceCount--;
    return 0;
}
