/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose one of the shape methods
 * @date 03-11-2023
 */
public class Sphere extends ThreeDimensionalShape{
    public double radius;

    public Sphere(double radius){
        this.radius = radius;
    }
    public double getRadius(){ return radius;}

    public void setRadius(double radius){ this.radius = radius;}

    @Override
    public double getVolume(){
        return (4/3)*Math.PI*Math.pow(getRadius(), 3);
    }
    @Override
    public double getArea(){
        return (1/3)*Math.PI*Math.pow(getRadius(), 2);
    }
    @Override
    public String toString(){
        return String.format("Radius: %s%.2f", super.toString(), getRadius());
    }
}
