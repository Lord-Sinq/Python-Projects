/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Automobile extends LandTransportation {
    private String brand;
    private String model;

    public Automobile(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, String brand, String model){
        super(type, cost, isTicket, averageSpeed, passengersAllowed, "Gasoline");
        this.brand = brand;
        this.model = model;

    }
    public String getBrand(){ return brand;}
    public void setBrand(String brand){ this.brand = brand;}
    public String getModel(){ return model;}
    public void setModel(String model){ this.model = model;}

    @Override
    public String toString(){ return String.format(super.toString()+"   Brand: "+getBrand()+"   Model: "+getModel()+ "\n");}

    @Override
    public String travelInstructions() {
        return ("Thank you for choosing this " + this.getType() + "! " + "To pick up your vehicle, please head to the rental center between the hours of 7am-6pm. Please keep in mind that all passengers interested in driving the automobile are required to have a valid driver's license. We look forward to seeing you!" );
    }
}
