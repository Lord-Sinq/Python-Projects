/**
 * @purpose Transportation
 * @author DeYoung,Pare,Painter
 * @date 19-10-2023
 * @section CSC 331-003
 */
public class Helicopter {
    //class attributes
    private double height;
    //constructor
    public Helicopter(String type, double cost, boolean isTicket, double averageSpeed, int passengersAllowed, int engines, double height){
        super(type,cost,isTicket,averageSpeed,passengersAllowed,engines);
        this.height = height;
    }
    public double getHeight(){return height;}
    public void setHeight(double height){this.height = height;}

    @Override
    public String toString(){ return super.toString()+"\nHeight: "+height;}
}
