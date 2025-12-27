import random

class GameUtil:
    _players = {}       # player_id -> current HP
    _player_max_hp = {} # player_id -> max HP
    _dice = {}          # die_id -> sides

    _next_player_id = 1
    _next_die_id = 1

    # ===============================
    # OBJECT CREATION
    # ===============================
    @classmethod
    def new(cls, type_, value=None):
        if type_ == "player":
            if value is None or value <= 0:
                raise ValueError("Player must start with positive HP.")
            pid = cls._next_player_id
            cls._players[pid] = value
            cls._player_max_hp[pid] = value
            cls._next_player_id += 1
            return pid

        elif type_ == "die":
            if value is None or value < 2:
                raise ValueError("Die must have at least 2 sides.")
            did = cls._next_die_id
            cls._dice[did] = value
            cls._next_die_id += 1
            return did

        else:
            raise ValueError("Unknown object type.")

    # ===============================
    # EXISTENCE CHECK
    # ===============================
    @classmethod
    def exists(cls, type_, obj_id):
        if type_ == "player":
            return obj_id in cls._players
        elif type_ == "die":
            return obj_id in cls._dice
        return False

    # ===============================
    # PLAYER HP SYSTEM
    # ===============================
    @classmethod
    def setMaxHP(cls, player_id, max_hp):
        if not cls.exists("player", player_id):
            return "Error: Player does not exist."
        if max_hp <= 0:
            return "Error: Max HP must be positive."
        cls._player_max_hp[player_id] = max_hp
        cls._players[player_id] = min(cls._players[player_id], max_hp)
        return True

    @classmethod
    def atk(cls, damage, player_id):
        if not cls.exists("player", player_id):
            return "Error: Player does not exist."
        if damage < 0:
            return "Error: Damage must be positive."
        cls._players[player_id] -= damage
        if cls._players[player_id] < 0:
            cls._players[player_id] = 0
        return cls._players[player_id]

    @classmethod
    def heal(cls, amount, player_id):
        if not cls.exists("player", player_id):
            return "Error: Player does not exist."
        if amount < 0:
            return "Error: Heal amount must be positive."
        cls._players[player_id] += amount
        if cls._players[player_id] > cls._player_max_hp[player_id]:
            cls._players[player_id] = cls._player_max_hp[player_id]
        return cls._players[player_id]

    @classmethod
    def getHP(cls, player_id):
        if not cls.exists("player", player_id):
            return "Error: Player does not exist."
        return cls._players[player_id]

    # ===============================
    # DICE SYSTEM
    # ===============================
    @classmethod
    def roll(cls, die_id):
        if not cls.exists("die", die_id):
            return "Error: Die does not exist."
        return random.randint(1, cls._dice[die_id])

    # ===============================
    # DELETE SYSTEM
    # ===============================
    @classmethod
    def delete(cls, type_, obj_id):
        if type_ == "player":
            if not cls.exists("player", obj_id):
                return "Error: Player does not exist."
            del cls._players[obj_id]
            del cls._player_max_hp[obj_id]
            return True
        elif type_ == "die":
            if not cls.exists("die", obj_id):
                return "Error: Die does not exist."
            del cls._dice[obj_id]
            return True
        else:
            return "Error: Unknown object type."

    # ===============================
    # DEBUG / INFO TOOLS
    # ===============================
    @classmethod
    def listPlayers(cls):
        return dict(cls._players)

    @classmethod
    def listDice(cls):
        return dict(cls._dice)
