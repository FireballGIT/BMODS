const GameUtil = {
    _players: {},
    _playerMaxHP: {},
    _dice: {},
    _nextPlayerId: 1,
    _nextDieId: 1,

    newPlayer(startingHP) {
        if (startingHP <= 0) throw new Error("Player must start with positive HP.");
        const id = this._nextPlayerId++;
        this._players[id] = startingHP;
        this._playerMaxHP[id] = startingHP;
        return id;
    },

    newDie(sides) {
        if (sides < 2) throw new Error("Die must have at least 2 sides.");
        const id = this._nextDieId++;
        this._dice[id] = sides;
        return id;
    },

    existsPlayer(id) {
        return id in this._players;
    },

    existsDie(id) {
        return id in this._dice;
    },

    setMaxHP(playerId, maxHP) {
        if (!this.existsPlayer(playerId)) return "Error: Player does not exist.";
        if (maxHP <= 0) return "Error: Max HP must be positive.";
        this._playerMaxHP[playerId] = maxHP;
        this._players[playerId] = Math.min(this._players[playerId], maxHP);
        return true;
    },

    atk(damage, playerId) {
        if (!this.existsPlayer(playerId)) return "Error: Player does not exist.";
        if (damage < 0) return "Error: Damage must be positive.";
        this._players[playerId] = Math.max(this._players[playerId] - damage, 0);
        return this._players[playerId];
    },

    heal(amount, playerId) {
        if (!this.existsPlayer(playerId)) return "Error: Player does not exist.";
        if (amount < 0) return "Error: Heal amount must be positive.";
        this._players[playerId] = Math.min(this._players[playerId] + amount, this._playerMaxHP[playerId]);
        return this._players[playerId];
    },

    getHP(playerId) {
        if (!this.existsPlayer(playerId)) return "Error: Player does not exist.";
        return this._players[playerId];
    },

    roll(dieId) {
        if (!this.existsDie(dieId)) return "Error: Die does not exist.";
        return Math.floor(Math.random() * this._dice[dieId]) + 1;
    },

    deletePlayer(id) {
        if (!this.existsPlayer(id)) return "Error: Player does not exist.";
        delete this._players[id];
        delete this._playerMaxHP[id];
        return true;
    },

    deleteDie(id) {
        if (!this.existsDie(id)) return "Error: Die does not exist.";
        delete this._dice[id];
        return true;
    },

    listPlayers() {
        return { ...this._players };
    },

    listDice() {
        return { ...this._dice };
    }
};

module.exports = GameUtil;
