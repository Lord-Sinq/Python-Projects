/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Plane extends AirTransportation {
    private String startDestination;
    private String endDestination;
    private String departureTime;
    //constructor
    public Plane(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, int altitude, String startDestination, String endDestination, String departureTime){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, engines, altitude);
        this.startDestination = startDestination;
        this.endDestination = endDestination;
        this.departureTime = departureTime;
    }

    public String getStartDestination() {return startDestination;}
    public String getEndDestination() {return endDestination;}
    public String getDepartureTime() {return departureTime;}


    public void setStartDestination(String startDestination) {this.startDestination = startDestination;}

    public void setEndDestination(String endDestination) {this.endDestination = endDestination;}

    public void setDepartureTime(String departureTime) {this.departureTime = departureTime;}

    @Override
    public String toString(){ return String.format(super.toString() + "   Start: " + getStartDestination() + "   End: " + getEndDestination() + "   Departure Time: " + getDepartureTime() + "\n");}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "The plane will be departing at " + getDepartureTime() + " from " + getStartDestination() + " and arriving at " + getEndDestination() + ". As a reminder, please arrive at the start destination 2 hours prior to departure in order to get through customs stress-free. Enjoy your flight!" );
    }
}
