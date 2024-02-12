/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Helicopter extends AirTransportation{
    public Helicopter(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, int altitude){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, engines, altitude);
    }

    @Override
    public String toString(){ return String.format(super.toString() + "\n");}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "We will be taking the scenic route over Oak Island, NC. Please understand that luggage and heavy baggage can not be brought onto the aircraft, as weight limits are tight. Please enjoy your trip, and as always, thank you for choosing us. " );
    }
}
