/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Bus extends LandTransportation{
    //constructor
    public Bus(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String fuelType){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, fuelType);
    }

    @Override
    public String toString() {
        return String.format(super.toString() + "\n");
    }

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "In order to reach your destination, you need to arrive at the departure location at 5am. Have a pleasant trip!" );
    }
}

