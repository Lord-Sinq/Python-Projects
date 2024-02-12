/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class LandTransportation extends Transportation {
    private String fuelType;
    public LandTransportation(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String fuelType){
        super(type, cost, isTicket, averageSpeed,passengersAllowed);
        this.fuelType = fuelType;
    }
    public String getFuelType(){ return fuelType;}
    public void setFuelType(String fuelType){ this.fuelType = fuelType;}
    @Override
    public String toString(){ return String.format(super.toString() +"   FuelType: "+ getFuelType());}
}
