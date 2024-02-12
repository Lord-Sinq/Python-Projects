/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Bus extends LandTransportation{
    //constructor
    public Bus(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String fuelType){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, fuelType);
    }
}

