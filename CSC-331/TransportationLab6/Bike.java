/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Bike extends LandTransportation{
    //constructor
    public Bike(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed,String fuelType){
        super(type, cost, isTicket, averageSpeed,passengersAllowed, fuelType);
    }

    @Override
    public String toString() {
        return String.format(super.toString() + "\n");
    }

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "Please pick up your bike at the service center located just outside the train station. All rentals must be returned by 11pm that night, or you will be charged for the following day. Enjoy your commute!" );
    }
}
