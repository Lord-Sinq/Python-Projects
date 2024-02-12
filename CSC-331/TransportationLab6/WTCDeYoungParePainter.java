/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */

/*
Hey team,  Marjorie here! I just made a few adjustments to the program to make it less text-heavy!

I have done the following things:
- adjusted all transportation classes and subclasses to better display the data. (table formatting)
- Split the main function into subsections to make it easier to read.
- Created a generateTransportation method, that takes the info for each subclass and creates its own object.
    It then puts this information into an array to use later in the program.
- Created a DisplayTransportation method, that displays the array into a table for easier viewing.
- I placed the while loop into its own function (called PromptUser) which lets us use recursion to
recall the prompts, in the event that the user changes their mind after a transportation object has been found.
- Created a method to get the number of passengers, calculate the cost, and display the travel information.
- added comments showing where polymorphism is used, and explains how.

TO DO:
- Create comment documentation for each method, showing parameter and return prompts.
 */

import java.util.Objects;
import java.util.Scanner;
public class WTCDeYoungParePainter {
    public static void main(String[] args) {

        //Activate scanner and generate the Transportation objects needed for the program.
        Scanner scanner = new Scanner(System.in);
        Transportation[] TravelOptions = generateTransportation();

        System.out.print("Welcome to the travel software! \nThis project is designed to give you a list of options to make the best of your travel destination needs!\n\n");

        //Display the information for the user.
        //DisplayTransportation(TravelOptions);

        //Start the prompts and while loop.
        PromptUser(scanner, TravelOptions);

        scanner.close();
    }

    public static Transportation[] generateTransportation(){
        //This method generates an array of transportation objects that we can easily access later.

        //Instead of making separate arrays for each different kind of transportation, we can use inheritance to lump them all together into a single array for easier retrieval.

        //Land
        Transportation bus = new Bus("Bus", 15.0, true, 45.0, 30, "Diesel");
        Transportation automobile = new Automobile("Automobile", 150.0, false, 55.0, 5, "Honda", "CRV");
        Transportation bike = new Bike("Bike", 30.0, false, 10.0, 1, "Pedals");
        Transportation train = new Train("Train", 25.0, true, 80.0, 200, "Coal");
        //Air
        Transportation plane = new Plane("Plane", 200.0, true, 500.0, 60, 2, 10000, "ILM", "SEA", "12:30am");
        Transportation hotAirBalloon = new HotAirBalloon("Hot Air Balloon", 25.0, false, 15.0, 4, 1,3000);
        Transportation helicopter = new Helicopter("Helicopter", 60.0, true, 50.0, 8, 1,5000);
        Transportation dirigible = new Dirigible("Dirigible", 50.0, true, 40.0, 60,4, 6000);
        //Water
        Transportation boat = new Boat("Boat", 15.0, false, 45.0, 8, "Fishing boat",0);
        Transportation ship = new Ship("Ship", 30.0, true, 30.0, 150, "Cruse ship",0);
        Transportation submarine = new Submarine("Submarine", 50.0, true, 20.0, 30, "Submarine",5000);

        return new Transportation[] {bus, automobile, bike, train, plane, hotAirBalloon, helicopter, dirigible, boat, ship, submarine};
    }

    public static void DisplayTransportation(Transportation[] transportation, String type){
        //Displays a table of all available transportation methods.

        System.out.printf("%15s%8s%12s%15s%18s%n", "Type", "Cost", "Purchase", "Average Speed", "Max Passengers");
        System.out.print("-".repeat(150) + "\n");

        //Display the appropriate options for the given transportation type.

        //This is one of the locations where polymorphism is used.
        //In order to just display the necessary information, a method in Transportation is called to display only the base data. We also use polymorphism and the function 'instanceof' in order to more easily locate the items we are looking for within the array of Transportation objects.
        if(Objects.equals(type, "Land")) {
            for (Transportation transport : transportation) {
                if (transport instanceof LandTransportation) {
                    System.out.println(transport.displayBaseData());
                }
            }
        } else if (Objects.equals(type, "Air")) {
            for (Transportation transport : transportation) {
                if (transport instanceof AirTransportation) {
                    System.out.println(transport.displayBaseData());
                }
            }

        }else   //Otherwise, it's water!
        {
            for (Transportation transport : transportation) {
                if (transport instanceof WaterTransportation) {
                    System.out.println(transport.displayBaseData());
                }
            }
        }

    }

    public static Transportation findTransportation(String type, Transportation[] transportation){
        //Search for a matching type in the transportation array

        for (Transportation transport : transportation) {

            //If it's a match, return it! Otherwise, return null.
            if(transport.getType().equalsIgnoreCase(type)){
                System.out.println("Here is the available transportation option for " + type + ":");
                System.out.printf("%15s%8s%12s%15s%18s%25s%n", "Type", "Cost", "Purchase", "Average Speed", "Max Passengers", "Extras");
                System.out.print("-".repeat(150) + "\n");

                //Here we use the overriden toString method for each subclass of transportation to display ALL the relevant data for that object type. This is another use of polymorphism, as different Transportation objects have different bits of extra data related to their typing.
                System.out.println(transport);

                return transport;
            }
        }

        return null;
    }

    public static void PromptUser(Scanner scanner, Transportation[] TravelOptions) {
        //Handles the while loop that prompts the user for valid data.

        Transportation selectedTransportation = null;

        //While there's not valid transportation object...
        while (selectedTransportation == null) {

            //Prompt the user
            System.out.println("Select a type of transportation (Land, Air, Water):");
            String selectedType = scanner.nextLine();

            //Check which kind of transportation the user is looking for
            switch (selectedType) {
                case ("Land"):

                    //displays the information relating to the selected transportation type (land, air, water).
                    DisplayTransportation(TravelOptions, selectedType);

                    //prompt the user to be specific, now that the correct type of transportation has been established.
                    System.out.println("Select land transportation (Bus, Automobile, Bike, Train): ");
                    selectedType = scanner.nextLine();

                    // Search the array and return the match!
                    selectedTransportation = findTransportation(selectedType, TravelOptions);
                    break;

                case ("Air"):

                    DisplayTransportation(TravelOptions, selectedType);

                    System.out.println("Select air transportation (Plane, Hot Air Balloon, Helicopter, Dirigible): ");
                    selectedType = scanner.nextLine();

                    //Search the array and find the match!
                    selectedTransportation = findTransportation(selectedType, TravelOptions);
                    break;

                case ("Water"):

                    DisplayTransportation(TravelOptions, selectedType);

                    System.out.println("Select water transportation (Ship, Boat, Submarine): ");
                    selectedType = scanner.nextLine();

                    //Search array and return match
                    selectedTransportation = findTransportation(selectedType, TravelOptions);
                    break;

                default:
                    //If it isn't one of these 3 types, it's invalid. Notify the user and continue the loop.
                    System.out.println("Invalid choice. Please select a valid transportation mode:");
            }
        }

        //Prompt user if they are okay with this choice after validating the method of transportation.
        System.out.print("Is this the mode of transportation you want to use (yes/no)? ");
        String confirmation = scanner.nextLine();

        //If they're good with it, move onto the next thing!
        if (confirmation.equalsIgnoreCase("yes") || confirmation.equalsIgnoreCase("y")) {
            System.out.println("That's great! Lets continue!");

            //Call the next method here! (Probably asking the number of passengers and displaying some kind of cost)
            getPassengers(scanner, selectedTransportation);

        } else {

            //If they don't like that option, simply recall the method to have them start the input process over again.
            System.out.println("I'm sorry you were not satisfied with that travel method. Lets try again:");
            PromptUser(scanner, TravelOptions);
        }

    }

    public static void getPassengers(Scanner scanner, Transportation travelMethod){
        //This method is used to get the number of passengers, calculate and display the total cost, and then print out the travel instructions.

        System.out.print("How many passengers are going on this trip? The maximum number of passengers for this method of transportation is: " + travelMethod.getPassengersAllowed());
        int passengers = scanner.nextInt();

        if(passengers > travelMethod.getPassengersAllowed() || passengers < 0){
            //if the number is invalid, recall the method to let them retry.
            System.out.println("I am sorry, that is more passengers than are available. Please try again.");
            getPassengers(scanner, travelMethod);

        }else{
            // calculate cost
            System.out.println("The total cost for " + passengers + " passengers is $"+ (travelMethod.getCost() * passengers) + ".");

            //display the travel instructions
            //This is the last instance of polymorphism. Each travel method has its own travel instructions that use a function override (Transportation.travelInstructions) to display their unique instructions on how to prepare for that trip.
            System.out.println("\nHere are the instructions for your chosen method of travel:");
            System.out.println(travelMethod.travelInstructions() + "\n");
        }
    }

}
