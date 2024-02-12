/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class WaterTransportation extends Transportation{
    private String watercraftType;
    public WaterTransportation(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String watercraftType){
        super(type, cost, isTicket, averageSpeed,passengersAllowed);
        this.watercraftType = watercraftType;
    }
    public String getWatercraftType(){ return watercraftType;}
    public void setWatercraftType(String watercraftType){ this.watercraftType = watercraftType;}

    @Override
    public String toString(){ return super.toString()+"\nWatercraft Type: "+watercraftType;}
}
