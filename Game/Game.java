package Game;

import java.util.Collections;

import static Game.PlayerList.player_list;

public class Game {
    public static String winner = null;

    public Game(){
        chooseRoles();
    }


    //adds new player with the players username and adds the player to the player_list
    public static void new_player(String username){
        Player player = new Player();
        player.username = username;
        PlayerList.add_player(player);

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

    //checks how many crewmates are alive and if there is only one, impostor wins
    private static void checkDeathWin() {
        int number_of_players = player_list.size();
        int alive_crewmates = 0;
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).status == "alive" && player_list.get(i).role == "crewmate"){
                alive_crewmates = alive_crewmates + 1;
            }
        }

        if (alive_crewmates == 1){
            impostor_win();
        }
    }

    //changes the status of an alive player to dead. If the player who died was an impostor, crewmates win.
    public static void playerDead(String username){
        int number_of_players = player_list.size();
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).username == username){
                player_list.get(i).status = "dead";

                if(player_list.get(i).role == "impostor"){
                    crewmate_win();
                }

            }
        }
        checkDeathWin();

    }


    public static void impostor_win() {
        winner = "Impostor wins";
        System.out.println(winner);
    }

    public static void crewmate_win(){
        winner = "Crewmates win";
        System.out.println(winner);
    }



}
