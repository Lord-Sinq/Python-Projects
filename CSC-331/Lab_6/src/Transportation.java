/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Transportation {
    private String type;
    private double cost;
    private boolean isTicket;
    private double averageSpeed;
    private int passengersAllowed;
    //constructor
    public Transportation(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed){
        this.type = type;
        this.cost = cost;
        this.isTicket = isTicket;
        this.averageSpeed = averageSpeed;
        this.passengersAllowed = passengersAllowed;
    }
    @Override
    public String toString(){
        return "Type: "+type+"\nCost: $"+cost+"\nIS Ticket: "+isTicket+"\nAverage Speed: "+averageSpeed+" mph\nPassengers Allowed: "+passengersAllowed;
    }
}
