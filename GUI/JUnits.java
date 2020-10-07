package GUI;
import Game.Game;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static Game.PlayerList.player_list;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JUnits {
    @Test
    public void playersAddedToGame() {
        Main tester = new Main(); // MyClass is tested

        Main.new_player("playerone");
        Main.new_player("playertwo");
        Main.new_player("playerthree");
        Main.new_player("playerfour");
        Main.new_player("playerfive");
        Main.new_player("playersix");
        Main.new_player("playerseven");
        Main.new_player("playereight");
        Main.new_player("playernine");
        Main.new_player("playerten");
        assertEquals("playerone", player_list.get(0).username);
        assertEquals("playertwo", player_list.get(1).username);
        assertEquals("playerseven", player_list.get(6).username);
        assertEquals("playerten", player_list.get(9).username);
    }

    @Test
    public void OneImpostorChosen(){
        Main tester = new Main(); // MyClass is tested

        Main.new_player("playerone");
        Main.new_player("playertwo");
        Main.new_player("playerthree");
        Main.new_player("playerfour");
        Main.new_player("playerfive");
        Main.new_player("playersix");
        Main.new_player("playerseven");
        Main.new_player("playereight");
        Main.new_player("playernine");
        Main.new_player("playerten");
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



}
