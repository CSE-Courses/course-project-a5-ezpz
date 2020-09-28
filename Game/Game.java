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
                player_list.get(0).role = "impostor";
            }
            else{
                player_list.get(i).role = "crewmate";
            }
        }
    }

    //changes the status of an alive player to dead. If the player who died was an impostor, crewmates win.
    void playerDead (String username){
        int number_of_players = player_list.size();
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).username == username){
                player_list.get(i).status = "dead";
                //if impostor dies, crewmates wins. function not added yet
                /*if(player_list.get(i).role == "impostor"){
                    crewmate_win();
                }*/

            }
        }
        checkDeathWin();

    }

    //checks how many crewmates are alive and if there is only one, impostor wins
    private void checkDeathWin() {
        int number_of_players = player_list.size();
        int alive_crewmates = 0;
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).status == "alive" && player_list.get(i).role == "crewmate"){
                alive_crewmates = alive_crewmates + 1;
            }
        }
        //if there is only one crewmate left, impostor wins, function not added yet
        /*if (alive_crewmates == 1){
            impostor_win();
        }*/
    }

}
