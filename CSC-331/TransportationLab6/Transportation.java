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

    public String toString(){
        return displayBaseData();
    }

    //Added a method to simplify the display in the event that only the base data is needed.
    public String displayBaseData(){
        String tempVal = "";
        if(isTicket){
            tempVal = "Ticket";
        }else{
            tempVal = "Rental";
        }

        return  String.format("%15s%8s%12s%15s%18s", getType(), getCost(), tempVal, (getAverageSpeed() + " mph"), getPassengersAllowed());
    }

    //This method is used to display the different travel instructions for each
    //method of transportation.
    public String travelInstructions() {
        return null;
    }

    public String getType() {
        return this.type;
    }

    public double getCost() {
        return this.cost;
    }

    public boolean getTicket() {
        return this.isTicket;
    }

    public double getAverageSpeed() {
        return this.averageSpeed;
    }

    public int getPassengersAllowed() {
        return this.passengersAllowed;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setCost(double cost) {
        this.cost = cost;
    }

    public void setTicket(boolean isTicket) {
        this.isTicket = isTicket;
    }

    public void setAverageSpeed(double averageSpeed) {
        this.averageSpeed = averageSpeed;
    }

    public void setPassengersAllowed(int passengersAllowed) {
        this.passengersAllowed = passengersAllowed;
    }
}
