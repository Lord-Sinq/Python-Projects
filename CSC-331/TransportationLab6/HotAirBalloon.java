/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class HotAirBalloon extends AirTransportation {
    public HotAirBalloon(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, int altitude){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, engines, altitude);
    }

    @Override
    public String toString(){ return String.format(super.toString() + "\n");}

    @Override
    public String travelInstructions() {
        return ("The " + this.getType() + " is a wonderful way to experience air travel. We depart the Myrtle Beach landing pad at 1pm in order to take in those breathtaking views. You and your guests should arrive 30 minutes early to receive a short training lecture and instructions on how to maximize your experience. Have a great flight!" );
    }
}

