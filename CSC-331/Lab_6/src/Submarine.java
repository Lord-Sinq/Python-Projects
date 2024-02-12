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
    public String toString(){ return super.toString()+"\nDepth Limit: "+depthLimit+" meters";}
}

