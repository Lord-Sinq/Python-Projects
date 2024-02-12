/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose one of the shape methods
 * @date 03-11-2023
 */
public class Circle extends TwoDimensionalShape{
    public double radius;

    public Circle(double radius){
        this.radius = radius;
    }
    public double getRadius(){ return radius;}
    public void setRadius(double radius){ this.radius = radius;}

    @Override
    public double getArea(){
        return Math.PI*Math.pow(getRadius(), 2);
    }
    @Override
    public String toString(){
        return String.format("Radius: %s%.2f\n", super.toString(), getRadius());
    }
}