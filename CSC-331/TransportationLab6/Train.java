/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Train extends LandTransportation{
    public Train(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String fuelType){
        super(type, cost, isTicket, averageSpeed,passengersAllowed,fuelType);
    }

    @Override
    public String toString() {
        return String.format(super.toString() + "\n");
    }

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "In order to reach your destination, you need to arrive at the departure location at 8am. This train travels through the mountains of North Carolina, giving you scenic views in the comfort of our luxury traveller's cabins. You will arrive at your destination feeling refreshed. Have a pleasant trip!" );
    }
}
