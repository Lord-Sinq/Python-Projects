/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Ship extends WaterTransportation{
    //class attributes
    private int depthLimit;
    //constructor
    public Ship(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String watercraftType, int depthLimit){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, watercraftType);
        this.depthLimit = depthLimit;
    }
    public int getDepthLimit(){return depthLimit;}
    public void setDepthLimit(int depthLimit){this.depthLimit = depthLimit;}

    @Override
    public String toString(){ return String.format(super.toString()+"   Depth Limit: "+getDepthLimit()+" meters" + "\n");}

    @Override
    public String travelInstructions() {
        return ("Welcome aboard the " + this.getType() + "! " + "In order to reach your destination, you need to arrive at the ship dock no later than 10am. Drinks and snacks will be provided, as well as entertainment for you and any guests. Enjoy your stay!" );
    }
}
