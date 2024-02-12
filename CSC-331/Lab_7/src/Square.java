/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose one of the shape methods
 * @date 03-11-2023
 */
public class Square extends TwoDimensionalShape{
    public double length;

    public Square(double length){
        this.length = length;
    }
    public double getLength(){ return length;}
    public void setLength(double length){ this.length = length;}

    @Override
    public double getArea(){
        return Math.pow(getLength(), 2);
    }
    @Override
    public String toString() {
        return String.format("Length: %s%.2f\n", super.toString(), getLength());
    }
}
