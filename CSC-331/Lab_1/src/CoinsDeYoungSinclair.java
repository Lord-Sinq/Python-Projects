/**
 * Program Purpose: Basic Python Program to convert to Java
 * Name: Sinclair DeYoung
 * Data: 25.08.2023
 * Section: CSC 331-003
 */

public class CoinsDeYoungSinclair {
    public static void main(String[] args){
        System.out.println("This program displays the results of 1,000,000 coin tosses.");
        int count = 1;
        int heads = 0;
        int tails = 0;
        // while loop till count is grater then 1000000
        while (count <= 1000000){
            int flip = (int) (2*Math.random());
            // checks if the flip was zero to add to heads
            if (flip == 0){
                heads += 1;
            }
            // adds the other answer to tails
            else{
                tails += 1;
            }
            count += 1;
        }
        // desplay the results
        System.out.println("Heads:"+ heads);
        System.out.println("Tails:"+ tails);

    }
}
