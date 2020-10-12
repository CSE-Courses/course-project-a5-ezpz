package GUI;

import Game.Game;
import org.junit.jupiter.api.Test;

import static Game.PlayerList.player_list;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class JUnits {

    //tests to make sure players are added to the game by new_player
    @Test
    public void playersAddedToGame() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        assertEquals("playerone", player_list.get(0).username);
        assertEquals("playertwo", player_list.get(1).username);
        assertEquals("playerseven", player_list.get(6).username);
        assertEquals("playerten", player_list.get(9).username);
    }

    //tests to ensure that there is only one impostor chosen and every other player is a crewmate
    @Test
    public void OneImpostorChosen(){
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
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

    //tests playerDead method to make sure only the player used in the argument dies
    @Test
    public void playerWillDie(){
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        Game.playerDead(player_list.get(0).username);
        Game.playerDead(player_list.get(3).username);
        Game.playerDead(player_list.get(7).username);
        Game.playerDead(player_list.get(9).username);
        assertEquals("dead", player_list.get(0).status);
        assertEquals("dead", player_list.get(3).status);
        assertEquals("dead", player_list.get(7).status);
        assertEquals("dead", player_list.get(9).status);
        assertEquals("alive", player_list.get(2).status);
        assertEquals("alive", player_list.get(8).status);
    }

    //makes sure all players are alive at the start of a game
    @Test
    public void playersAliveAtStart(){
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        for (int i = 0; i < player_list.size(); i++){
            assertEquals("alive", player_list.get(i).status);
        }

    }


    //tests to make sure that crewmates win if impostor dies
    @Test
    public void crewmatesWinIfImposterDies() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role == "impostor"){
                Game.playerDead(player_list.get(i).username);
            }
        }
        assertEquals("Crewmates win", Game.winner);


    }

    //tests to make sure the impostor wins if there is only one crewmate alive
    @Test
    public void impostorWinsIfThereIsOneCremateLeft() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role != "impostor"){
                Game.playerDead(player_list.get(i).username);
            }
        }
        assertEquals("Impostor wins", Game.winner);


    }

    //tests to make sure no one dies if no votes are cast
    @Test
    public void nooneDiesIfNooneVotes() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
    }

    //tests to make sure no one dies if skip receives the most votes
    @Test
    public void noOneDiesIfSkipsReceivesMostVotes() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        player_list.get(1).voted = player_list.get(0).username;
        player_list.get(0).voted = "skip";
        player_list.get(2).voted = "skip";
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
    }

    //tests to make sure a player dies if they receive the most votes
    @Test
    public void playerDiesIfTheyReceiveTheMostVotes() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        player_list.get(1).voted = player_list.get(7).username;
        player_list.get(4).voted = player_list.get(7).username;
        player_list.get(2).voted = player_list.get(7).username;
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        int ind = Game.getPlayerIndex(player_list.get(7).username);
        for (int i = 0; i < player_list.size(); i++) {
            if (i == ind){
                assertEquals("dead", player_list.get(i).status);
            } else {
                assertEquals("alive", player_list.get(i).status);
            }
        }
    }

    //tests to make sure crewmates win if the impostor is voted out
    @Test
    public void crewmatesWinIfImpostorVotedOut() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        player_list.get(1).voted = player_list.get(0).username;
        player_list.get(4).voted = player_list.get(0).username;
        player_list.get(2).voted = player_list.get(0).username;
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        int ind = Game.getPlayerIndex(player_list.get(0).username);
        assertEquals("Crewmates win", Game.winner);
        }

    //tests to make sure no one dies if a vote is tied
    @Test
    public void noOneDiesInTiedVote() {
        Main tester = new Main(); // MyClass is tested

        Game.new_player("playerone");
        Game.new_player("playertwo");
        Game.new_player("playerthree");
        Game.new_player("playerfour");
        Game.new_player("playerfive");
        Game.new_player("playersix");
        Game.new_player("playerseven");
        Game.new_player("playereight");
        Game.new_player("playernine");
        Game.new_player("playerten");
        new Game();
        player_list.get(1).voted = player_list.get(6).username;
        player_list.get(0).voted = player_list.get(6).username;
        player_list.get(2).voted = player_list.get(7).username;
        player_list.get(3).voted = player_list.get(7).username;
        player_list.get(4).voted = player_list.get(8).username;
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
    }
    //tests to make sure prompt mess handles inputs correctly
    @Test
    public void num_is_1() { // Input is 1 for message 1
        Prompt tester = new Prompt(); // Prompt is tested
            assertEquals("Use the movement keys to do a dance party", tester.mess(1));
    }
    //tests to make sure prompt mess handles invalid inputs correctly
    @Test
    public void num_is_9() { // Input is 1 for message 9
        Prompt tester = new Prompt(); // Prompt is tested
        assertEquals("Use the movement keys to do a dance party", tester.mess(9));
    }
    //tests to make sure prompt mess handles inputs correctly

}

