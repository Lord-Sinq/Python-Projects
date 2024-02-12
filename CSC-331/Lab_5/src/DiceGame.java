/**
 * @purpose DiceGame
 * @author Sinclair DeYoung
 * @date 29-08-2023
 * @section CSC 331-003
 */
import java.util.Scanner;
public class DiceGame{
    public static void main(String[] arg){
        Scanner scanner = new Scanner(System.in);
        int[] sides1 = new int[] {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
        int[] sides2 = new int[] {00,10,20,30,40,50,60,70,80,90};
        // two dice
        Die die1 = new Die(20, "Blue", "Red","Gold", sides1);
        Die die2 = new Die(10, "Navy", "Orange", "Silver", sides2);

        System.out.println("First Die attributes:");
        die1.displayAttributes();
        System.out.println();

        System.out.println("Second Die attributes:");
        die1.displayAttributes();
        System.out.println();

        while (true){
            System.out.print("Do you want to play? (y/n): ");
            String playGame = scanner.nextLine().trim().toLowerCase();

            if (playGame.equals("y")){
                playDieGame(die1, die2);
            } else if (playGame.equals("n")){
                System.out.println("Goodbye.");
                break;
            }else{
                System.out.println("Error! please enter 'y' or 'n'.");
            }
        }

    }
    private static void playDieGame(Die die1, Die die2){
        Scanner scanner = new Scanner(System.in);
        int die1Rolls = 0;
        int die2Rolls = 0;

        System.out.println("Who do you think will win First Die or Second Die? Enter (f/s): ");
        String winGame = scanner.nextLine().trim().toLowerCase();

        while (true){
            int result1 = die1.roll();
            int result2 = die2.roll();

            if (winGame.equals("f")){
                System.out.println("You picked the First Die to win!");
            }else if (winGame.equals("s")){
                System.out.println("You picked the Second Die to win!");
            }else{
                System.out.println("Error: not a vaild input.");
                break;
            }

            System.out.println("Rolling first die: " + result1);
            System.out.println("Rolling second die: " + result2 + "\n");

            die1Rolls++;
            die2Rolls++;

            if (result1 == 10){
                System.out.println("First die rolled a 10.");
                if (winGame.equals("f")){
                    System.out.println("You won the game!");
                }
                System.out.println("Total rolls for the first die: " + die1Rolls);
                System.out.println("Total rolls for the second die: " + die2Rolls);
                break;
            } else if (result2 == 10){
                System.out.println("Second die rolled a 10.");
                if (winGame.equals("s")){
                    System.out.println("You won the game!");
                }
                System.out.println("Total rolls for the first die: " + die1Rolls);
                System.out.println("Total rolls for the second die: " + die2Rolls);
                break;
            }
        }
    }
}
