package GUI;
import Game.Game;
import org.junit.Rule;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static Game.PlayerList.player_list;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JUnits {
    @Test
    public void playersAddedToGame() {
        Main tester = new Main(); // MyClass is tested

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        assertEquals("playerone", player_list.get(0).username);
        assertEquals("playertwo", player_list.get(1).username);
        assertEquals("playerseven", player_list.get(6).username);
        assertEquals("playerten", player_list.get(9).username);
    }

    @Test
    public void OneImpostorChosen(){
        Main tester = new Main(); // MyClass is tested

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        new Game();
        int impostorCount = 0;
        int crewmateCount = 0;
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role == "crewmate"){
                crewmateCount = crewmateCount + 1;
            }
            else if (player_list.get(i).role == "impostor") {
                impostorCount = impostorCount + 1;
            }
        }
        assertEquals(9, crewmateCount);
        assertEquals(1, impostorCount);
    }


    @Test
    public void playerWillDie(){
        Main tester = new Main(); // MyClass is tested

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        new Game();
        tester.playerDead(player_list.get(0).username);
        tester.playerDead(player_list.get(3).username);
        tester.playerDead(player_list.get(7).username);
        tester.playerDead(player_list.get(9).username);
        assertEquals("dead", player_list.get(0).status);
        assertEquals("dead", player_list.get(3).status);
        assertEquals("dead", player_list.get(7).status);
        assertEquals("dead", player_list.get(9).status);
        assertEquals("alive", player_list.get(2).status);
        assertEquals("alive", player_list.get(8).status);
    }

    @Test
    public void playersAliveAtStart(){
        Main tester = new Main(); // MyClass is tested

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        new Game();
        for (int i = 0; i < player_list.size(); i++){
            assertEquals("alive", player_list.get(i).status);
        }

    }



    /*@Test
    public void crewmatesWinIfImposterDies() {


        Main tester = new Main(); // MyClass is tested

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        new Game();

        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role == "impostor"){
                tester.playerDead(player_list.get(i).username);
            }
        }

    }*/


}
