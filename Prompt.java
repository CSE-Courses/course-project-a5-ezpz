import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Prompt{

     public static void main(String []args){
         
         mess(getNum());
         
     }
     public static void mess(int n){ // This function takes in a random number to display a prompt 
         if( n == 0){
            System.out.println("Message 0");
         }
         else if( n == 1){
            System.out.println("Message 1");
         }
         else if( n == 2){
            System.out.println("Message 2");
         }
         else if( n == 3){
            System.out.println("Message 3");
         }
         else if( n == 4){
            System.out.println("Message 4");
         }
         else if( n == 5){
            System.out.println("Message 5");
         }
         else if( n == 6){
            System.out.println("Message 6");
         }
         else if( n == 7){
            System.out.println("Message 7");
         }
         else{
             System.out.print("No num");
         }
     }
     public static int getNum(){ // This function will pick a random number to output a message.
         // Integer[] otherList = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8}; // 8 numbers because only a max of 8 players can be eliminated
         ArrayList<Integer> nums = new ArrayList<Integer>(); //8 numbers because only a max of 8 players can be eliminated
         nums.add(1);
         nums.add(2);
         nums.add(3);
         nums.add(4);
         nums.add(5);
         nums.add(6);
         nums.add(7);
         nums.add(8);
         // highest index in nums array
         // Random rand = new Random()
         int param = (int)(Math.random()*nums.size() -1); // param for mess
         System.out.println(param); // debug
         nums.remove(param); // Delete the number so the same message won't be called twice.
         return param;
     }
}
