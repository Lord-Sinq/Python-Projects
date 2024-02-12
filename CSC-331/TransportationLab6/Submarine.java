/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Submarine extends WaterTransportation{
    //class attributes
    private int depthLimit;
    //constructor
    public Submarine(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String watercraftType, int depthLimit){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, watercraftType);
        this.depthLimit = depthLimit;
    }
    public int getDepthLimit(){return depthLimit;}
    public void setDepthLimit(int depthLimit){this.depthLimit = depthLimit;}

    @Override
    public String toString(){ return String.format(super.toString()+"   Depth Limit: "+ getDepthLimit() +" meters" + "\n");}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "In order to reach your destination, you need to arrive at the submarine dock location by 10am. It is important to ensure that all of your gear and equipment has no defects that could create an emergency. Have a pleasant trip!" );
    }
}

