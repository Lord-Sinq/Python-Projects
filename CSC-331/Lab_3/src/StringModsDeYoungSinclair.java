/**
 * @purpose Using user input of string to manipulate the date in the string
 * @author Sinclair DeYoung
 * @date 08.09.2023
 * @section CSC 331-003
 */
//I kept having an error message if I did not have package PACKAGE_NAME
package PACKAGE_NAME;
// import scanner
import java.util.Scanner;

public class StringModsDeYoungSinclair{
    public static void main(String[] args){
        //Prompt the user to enter two strings, an integer, and a double.
        // Call the other three methods. Display the result of the method calls.
        // Repeat until the user does not want to continue.

        // boolean argument
        boolean start = true;
        //while loop to keep playing
        while(start) {
            //scanner
            Scanner scanner = new Scanner(System.in);

            // string 1
            System.out.println("Type a string out:");
            String str_1 = scanner.nextLine();
            // string 2
            System.out.println("Type another string:");
            String str_2 = scanner.nextLine();
            //integer
            System.out.println("Type another integer:");
            int int_1 = scanner.nextInt();
            //double
            System.out.println("Type another double:");
            double double_1 = scanner.nextDouble();
            scanner.nextLine();

            // send the strings, int, and double through the other methods
            String results_1 = stringMod(str_1, int_1);
            String results_2 = stringMod(str_1, double_1);
            String results_3 = stringMod(str_1, str_2);

            // print the results
            System.out.println("The first method: " + results_1);
            System.out.println("The Second method: " + results_2);
            System.out.println("The third method: " + results_3);

            // ask the user if they want to go again
            System.out.println("Do you want to start over (y/n): ");
            String input = scanner.nextLine();

            // if statement to break the loop
            if(!input.equalsIgnoreCase("y")){
                start = false;
            }
        }
        //while loop ended
        Scanner bye = new Scanner(System.in);
        System.out.println("Goodbye.");
        bye.close();
    }
    /**
     * removes evey int_1 character from the input string
     *
     * @param str_1 string input
     * @param int_1 integer input
     * @return the modded string
     */
    public static String stringMod(String str_1, int int_1){
        //Has a string and an integer (n) for parameters.
        //Build an object to change the string
        StringBuilder modString = new StringBuilder();
        // for loop to determine the length of the string
        // and store that value in i
        for (int i = 0; i < str_1.length(); i++){
            // if statement to check if the current character
            // should be excluded based on the value of int_1.
            if ((i+1) % int_1 != 0){
                modString.append(str_1.charAt(i));
            }
        }
        // return newly modded string
        return modString.toString();
    }
    /**
     * replaces all 'e' characters in the input with double value
     *
     * @param str_1 string input
     * @param double_1 double input
     * @return the modded string
     */
    public static String stringMod(String str_1, double double_1){
        //Has a string and a double for parameters.
        // first convert the double value into a string.
        String numStr = Double.toString(double_1);
        // then replace all "e" characters with the new string and return this value.
        return str_1.replaceAll("e", numStr);
    }
    /**
     * alternates character from two strings
     *
     * @param str_1 string 1 input
     * @param str_2 string 2 input
     * @return the modded string
     */
    public static String stringMod(String str_1, String str_2){
        //Has two strings as parameters.
        // make an empty object to manipulate the string
        StringBuilder modString = new StringBuilder();
        // minLength stores the min length of string 1, string 2
        // so make the loop iterate up to the length of the shorter string
        int minLength = Math.min(str_1.length(), str_2.length());
        //for loop to save each variable of the string in its position and saves it to modString.
        //combining each string one variable at a time.
        for(int i = 0; i < minLength; i++){
            modString.append(str_1.charAt(i));
            modString.append(str_2.charAt(i));
        }
        // checks to see if string 1 is longer then string 2.
        // if so then it appends the rest of the string to the end of the new string.
        if(str_1.length() > str_2.length()){
            modString.append(str_1.substring(minLength));
        // else if string 2 is longer then string 1 then it appends the rest of the string
        // onto the end of the new string.
        } else if(str_2.length() > str_1.length()){
            modString.append(str_2.substring(minLength));
        }
        // return the stringBuilder object by converting it to a regular string.
        return modString.toString();
    }
}
