/**
 * @purpose Take users input and make a table of all unique Pythagorean triples
 * @author Sinclair DeYoung
 * @date 01.09.2023
 * @section CSC 331-003
 */
import java.util.Scanner;
import java.security.SecureRandom;

public class PythagoreanDeYoungSinclair {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        //giving the user options and asking for an input
        System.out.println("Choose an option:");
        System.out.println("1. Enter a maximum side length");
        System.out.println("2. Generate a random maximum side length");
        System.out.print("Enter your choice (1/2): ");
        int choice = input.nextInt();
        // switch to determin if the user chose options one or two
        switch(choice){
            // have the user input a max number
            case 1:
                System.out.print("Enter the Max value for the sides: ");
                int MAX = input.nextInt();
                // calls the pythTriples method with MAX as the input
                pythTriples(MAX);
                break;
            case 2:
                // Uses Secure Random to pick a number for the user within 1-100
                SecureRandom randomNumbers = new SecureRandom();
                int randomMax = 1 + randomNumbers.nextInt(100);
                System.out.println("Randomly generated max side length: " + randomMax);
                //uses the random max number as the input for the method pythTriples
                pythTriples(randomMax);
                break;
                // if 1 or 2 is not selected then print a str saying not valid input
            default:
                System.out.println("Not a Valid choice.");
        }

    }
    public static void pythTriples(int MAX) {
        // sets variables
        int result;
        int sideA, sideB, hypo;
        // print statement with titles to the rows
        System.out.println("Pythagorean Triples:");
        System.out.println("Side_A Side_B Hypotenus\n");

        // setting the first side
        for (sideA = 1; sideA <= MAX; sideA++) {
            // setting side 2 one higher then side 1 to stop duplication
            for (sideB = (sideA + 1); sideB <= MAX; sideB++) {
                // set hypo to not print duplicates
                for (hypo = (sideB + 1); hypo <= MAX; hypo++) {
                    result = (sideA * sideA) + (sideB * sideB);
                    // if conditions are met print the numbers
                    if (result == (hypo * hypo)) {
                        System.out.printf("%4d %6d %8d\n", sideA, sideB, hypo);
                    }
                }
            }
        }
    }
}