/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
import java.util.Scanner;
public class WTCDeYoungParePainter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while(true){
            //Land
            Transportation bus = new Bus("Bus", 15.0, true, 45.0, 30, "Diesel");
            Transportation automobile = new Automobile("Automobile", 150.0, false, 55.0, 5, "Honda", "CRV",);
            Transportation bike = new Bike("Bike", 30.0, false, 10.0, 1, "Pedals");
            Transportation train = new Train("Train", 25.0, true, 80.0, 200, "Coal");
            //Air
            Transportation plane = new Plane("Plane", 200.0, true, 500.0, 60, 2, 10000);
            Transportation hotAirBalloon = new HotAirBalloon("Hot Air Balloon", 25.0, false, 15.0, 4, 1,3000);
            Transportation helicopter = new Helicopter("Helicopter", 60.0, true, 50.0, 8, 1,5000);
            Transportation dirigible = new Dirigible("Dirigible", 50.0, true, 40.0, 60,4, 6000);
            //Water
            Transportation boat = new Boat("Boat", 15.0, false, 45.0, 8, "Fishing boat",0);
            Transportation ship = new Ship("Ship", 30.0, true, 30.0, 150, "Cruse ship",0);
            Transportation submarine = new Submarine("Submarine", 50.0, true, 20.0, 30, "Submarine",5000);

            System.out.println("Select a type of transportation (Land, Air, Water):");
            String selectedType = scanner.nextLine();
            Transportation selectedTransportation = null;

            if (selectedType.equalsIgnoreCase("Land")) {
                System.out.println("Select land transportation (bus, automobile, bike, train): ");
                selectedType = scanner.nextLine();
                if (selectedType.equalsIgnoreCase("bus")) {
                    selectedTransportation = bus;
                } else if (selectedType.equalsIgnoreCase("automobile")) {
                    selectedTransportation = automobile;
                } else if (selectedType.equalsIgnoreCase("bike")) {
                    selectedTransportation = bike;
                } else if (selectedType.equalsIgnoreCase("train")) {
                    selectedTransportation = train;
                }
            } else if (selectedType.equalsIgnoreCase("Air")) {
                System.out.println("Select land transportation (plane, hot air balloon, helicopter, dirigible): ");
                selectedType = scanner.nextLine();
                if (selectedType.equalsIgnoreCase("plane")) {
                    selectedTransportation = plane;
                } else if (selectedType.equalsIgnoreCase("hot air balloon")) {
                    selectedTransportation = hotAirBalloon;
                } else if (selectedType.equalsIgnoreCase("helicopter")) {
                    selectedTransportation = helicopter;
                } else if (selectedType.equalsIgnoreCase("dirigible")) {
                    selectedTransportation = dirigible;
                }
            } else if (selectedType.equalsIgnoreCase("Water")) {
                System.out.println("Select land transportation (ship, boat, submarine): ");
                selectedType = scanner.nextLine();
                if (selectedType.equalsIgnoreCase("ship")) {
                    selectedTransportation = ship;
                } else if (selectedType.equalsIgnoreCase("boat")) {
                    selectedTransportation = boat;
                } else if (selectedType.equalsIgnoreCase("submarine")) {
                    selectedTransportation = submarine;
                }
            }else {
                System.out.println("Invalid choice. Please select a valid transportation mode.");
                continue;
            }
            System.out.println("Transportation Information:");
            System.out.println(selectedTransportation);

            System.out.print("Is this the mode of transportation you want to use (yes/no)? ");
            String confirmation = scanner.nextLine();

            if(confirmation.equalsIgnoreCase("yes")){
                break;
            }
        }
        scanner.close();
    }
}
