/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose one of the shape methods
 * @date 03-11-2023
 */
public class Triangle extends TwoDimensionalShape{
    public double height, base;

    public Triangle(double height, double base){
        this.height = height;
        this.base = base;
    }
    public double getHeight(){ return height;}
    public double getBase(){ return base;}

    public void setHeight(double height){ this.height = height;}
    public void setBase(double base){ this.base = base;}

    @Override
    public double getArea(){
        return (getBase()*getHeight())/2;
    }
    @Override
    public String toString(){
        return String.format("Base: %s%.2f\nHeight: %.2f\n", super.toString(), getBase(), getHeight());
    }
}