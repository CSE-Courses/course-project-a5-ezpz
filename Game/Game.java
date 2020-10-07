package Game;

import java.util.ArrayList;
import java.util.Collections;

import static Game.PlayerList.player_list;

public class Game {
    public Game(){
        chooseRoles();
    }



    //assigns impostor randomly to one player and makes every other player a crewmate
    void chooseRoles (){
        int number_of_players = player_list.size();
        Collections.shuffle(player_list);
        for (int i = 0; i < number_of_players; i++){
            if (i == 0){
                player_list.get(i).role = "impostor";
            }
            else{
                player_list.get(i).role = "crewmate";
            }
        }
    }



}
