/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Boat extends WaterTransportation{
    //class attributes
    private int motors;
    //constructor
    public Boat(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String watercraftType, int depthLimit){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, watercraftType);
        this.motors = motors;
    }
    public int getDepthLimit(){return motors;}
    public void setDepthLimit(int depthLimit){this.motors = motors;}

    @Override
    public String toString(){ return super.toString()+"   Number of Motors: "+ getDepthLimit() + "\n";}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "The boat docks at 12pm, so you will need to arrive with your passengers 2 hours prior. All luggage needs to be stored below deck, and no firearms or weapons are permitted. Thank you and have a pleasant trip!" );
    }
}
