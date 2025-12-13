# ===============================
# gameutil.py
# BAG Studios — Game Engine Core
# ===============================

import random

# ===============================
# INTERNAL STORAGE (PRIVATE)
# ===============================

_players = {}          # player_id -> current HP
_player_max_hp = {}    # player_id -> max HP
_dice = {}             # die_id -> sides

_next_player_id = 1
_next_die_id = 1


# ===============================
# OBJECT CREATION
# ===============================

def new(type, value=None):
    """
    new("player", starting_hp)
    new("die", sides)
    """
    global _next_player_id, _next_die_id

    if type == "player":
        if value is None or value <= 0:
            raise ValueError("Player must start with positive HP.")

        pid = _next_player_id
        _players[pid] = value
        _player_max_hp[pid] = value
        _next_player_id += 1
        return pid

    elif type == "die":
        if value is None or value < 2:
            raise ValueError("Die must have at least 2 sides.")

        did = _next_die_id
        _dice[did] = value
        _next_die_id += 1
        return did

    else:
        raise ValueError("Unknown object type.")


# ===============================
# EXISTENCE CHECK
# ===============================

def exists(type, obj_id):
    if type == "player":
        return obj_id in _players
    elif type == "die":
        return obj_id in _dice
    return False


# ===============================
# PLAYER HP SYSTEM
# ===============================

def setMaxHP(player_id, max_hp):
    if not exists("player", player_id):
        return "Error: Player does not exist."

    if max_hp <= 0:
        return "Error: Max HP must be positive."

    _player_max_hp[player_id] = max_hp
    _players[player_id] = min(_players[player_id], max_hp)
    return True


def atk(damage, player_id):
    if not exists("player", player_id):
        return "Error: Player does not exist."

    if damage < 0:
        return "Error: Damage must be positive."

    _players[player_id] -= damage
    if _players[player_id] < 0:
        _players[player_id] = 0

    return _players[player_id]


def heal(amount, player_id):
    if not exists("player", player_id):
        return "Error: Player does not exist."

    if amount < 0:
        return "Error: Heal amount must be positive."

    _players[player_id] += amount
    if _players[player_id] > _player_max_hp[player_id]:
        _players[player_id] = _player_max_hp[player_id]

    return _players[player_id]


def getHP(player_id):
    if not exists("player", player_id):
        return "Error: Player does not exist."
    return _players[player_id]


# ===============================
# DICE SYSTEM (UNLIMITED)
# ===============================

def roll(die_id):
    if not exists("die", die_id):
        return "Error: Die does not exist."

    return random.randint(1, _dice[die_id])


# ===============================
# DELETE SYSTEM
# ===============================

def delete(type, obj_id):
    """
    delete("player", id)
    delete("die", id)
    """
    if type == "player":
        if not exists("player", obj_id):
            return "Error: Player does not exist."

        del _players[obj_id]
        del _player_max_hp[obj_id]
        return True

    elif type == "die":
        if not exists("die", obj_id):
            return "Error: Die does not exist."

        del _dice[obj_id]
        return True

    else:
        return "Error: Unknown object type."


# ===============================
# DEBUG / INFO TOOLS
# ===============================

def listPlayers():
    """Returns all players and their current HP"""
    return dict(_players)


def listDice():
    """Returns all dice and their side counts"""
    return dict(_dice)
