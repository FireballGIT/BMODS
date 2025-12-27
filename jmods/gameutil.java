import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public final class GameUtil {
    private static Map<Integer, Integer> players = new HashMap<>();
    private static Map<Integer, Integer> playerMaxHP = new HashMap<>();
    private static Map<Integer, Integer> dice = new HashMap<>();

    private static int nextPlayerId = 1;
    private static int nextDieId = 1;
    private static Random random = new Random();

    // ===============================
    // OBJECT CREATION
    // ===============================
    public static int newPlayer(int startingHP) {
        if (startingHP <= 0) throw new IllegalArgumentException("Player must start with positive HP.");
        int id = nextPlayerId++;
        players.put(id, startingHP);
        playerMaxHP.put(id, startingHP);
        return id;
    }

    public static int newDie(int sides) {
        if (sides < 2) throw new IllegalArgumentException("Die must have at least 2 sides.");
        int id = nextDieId++;
        dice.put(id, sides);
        return id;
    }

    // ===============================
    // EXISTENCE CHECK
    // ===============================
    public static boolean existsPlayer(int id) {
        return players.containsKey(id);
    }

    public static boolean existsDie(int id) {
        return dice.containsKey(id);
    }

    // ===============================
    // PLAYER HP SYSTEM
    // ===============================
    public static String setMaxHP(int playerId, int maxHP) {
        if (!existsPlayer(playerId)) return "Error: Player does not exist.";
        if (maxHP <= 0) return "Error: Max HP must be positive.";
        playerMaxHP.put(playerId, maxHP);
        players.put(playerId, Math.min(players.get(playerId), maxHP));
        return "Success";
    }

    public static Object atk(int damage, int playerId) {
        if (!existsPlayer(playerId)) return "Error: Player does not exist.";
        if (damage < 0) return "Error: Damage must be positive.";
        int newHP = players.get(playerId) - damage;
        players.put(playerId, Math.max(newHP, 0));
        return players.get(playerId);
    }

    public static Object heal(int amount, int playerId) {
        if (!existsPlayer(playerId)) return "Error: Player does not exist.";
        if (amount < 0) return "Error: Heal amount must be positive.";
        int newHP = players.get(playerId) + amount;
        players.put(playerId, Math.min(newHP, playerMaxHP.get(playerId)));
        return players.get(playerId);
    }

    public static Object getHP(int playerId) {
        if (!existsPlayer(playerId)) return "Error: Player does not exist.";
        return players.get(playerId);
    }

    // ===============================
    // DICE SYSTEM
    // ===============================
    public static Object roll(int dieId) {
        if (!existsDie(dieId)) return "Error: Die does not exist.";
        return random.nextInt(dice.get(dieId)) + 1;
    }

    // ===============================
    // DELETE SYSTEM
    // ===============================
    public static String deletePlayer(int id) {
        if (!existsPlayer(id)) return "Error: Player does not exist.";
        players.remove(id);
        playerMaxHP.remove(id);
        return "Success";
    }

    public static String deleteDie(int id) {
        if (!existsDie(id)) return "Error: Die does not exist.";
        dice.remove(id);
        return "Success";
    }

    // ===============================
    // DEBUG / INFO TOOLS
    // ===============================
    public static Map<Integer, Integer> listPlayers() {
        return new HashMap<>(players);
    }

    public static Map<Integer, Integer> listDice() {
        return new HashMap<>(dice);
    }
}
