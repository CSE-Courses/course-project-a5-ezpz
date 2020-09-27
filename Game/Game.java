package Game;

import java.util.ArrayList;
import java.util.Collections;

public class Game {
    public Game(){
        chooseRoles();
    }
    void chooseRoles (){
        int number_of_players = PlayerList.player_list.size();
        Collections.shuffle(PlayerList.player_list);
        for (int i = 0; i < number_of_players; i++){

        }
    }

}
