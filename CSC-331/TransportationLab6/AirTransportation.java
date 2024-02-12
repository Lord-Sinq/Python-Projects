/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class AirTransportation extends Transportation{
    private int engines;
    private int altitude;
    public AirTransportation(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, int altitude){
        super(type, cost, isTicket, averageSpeed,passengersAllowed);
        this.engines = engines;
        this.altitude = altitude;
    }
    public int getEngines(){ return engines;}
    public int getAltitude() {return altitude;}

    public void setEngines(int engines){ this.engines = engines;}
    public void setAltitude(int altitude){this.altitude = altitude;}

    @Override
    public String toString(){ return super.toString()+"   Engines: "+ getEngines() + "   Altitude: " + getAltitude() + "ft";}
}

