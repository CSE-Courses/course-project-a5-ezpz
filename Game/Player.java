package Game;

//player class which holds player characteristics and adds them to list of player
public class Player {
    String username = null;
    public String role;
    public String status = "alive";
    public Player() {
        PlayerList.add_player(this);

    }
}
