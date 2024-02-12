/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Dirigible extends AirTransportation{
    //constructor
    public Dirigible(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, int altitude){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, engines, altitude);
    }

    @Override
    public String toString(){ return String.format(super.toString() + "\n");}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "The dirigible departs at 3pm, and the trip will take 2 hours. During your stay, you can enjoy the scenic views of the city, refreshments, and comfortable seating. We hope to see you then!" );
    }
}

