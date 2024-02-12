/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class AirTransportation extends Transportation{
    private int engines;
    public AirTransportation(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines){
        super(type, cost, isTicket, averageSpeed,passengersAllowed);
        this.engines = engines;
    }
    public int getEngines(){ return engines;}
    public void setEngines(int engines){ this.engines = engines;}

    @Override
    public String toString(){ return super.toString()+"\nEngines: "+engines;}
}

