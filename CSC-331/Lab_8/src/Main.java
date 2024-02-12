/**
 * @author Sinclair DeYoung
 * @purpose check to see if a work is a palindrome and adds it to a file
 * @section CSC 331-003
 * @date 06-11-2023
 */
import java.io.*;
import java.io.FileWriter;
import java.io.PrintWriter;

public class Main {
    public static void main(String[] args) {
        try{
            BufferedReader reader = new BufferedReader(new FileReader("wordList.txt"));
            String line;
            System.out.println("\nThis method takes the wordList.txt and checks for palindromes to add them to palindromeFile.txt");
            while ((line = reader.readLine()) != null){
                StringBuffer reversed = new StringBuffer(line).reverse();
                StringBuffer normal = new StringBuffer(line);
                String str1 = normal.toString();
                String str2 = reversed.toString();
                if (str1.equalsIgnoreCase(str2)){
                    FileWriter reStream = new FileWriter("palindromeFile.txt", true);
                    BufferedWriter out = new BufferedWriter(reStream);
                    out.write(str1);
                    out.write("\n");
                    out.close();
                }
            }
            reader.close();
            System.out.println("The file has been checked and the method is over.");
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}