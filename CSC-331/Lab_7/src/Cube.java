/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose one of the shape methods
 * @date 03-11-2023
 */
public class Cube extends ThreeDimensionalShape{
    private double edge;

    public Cube(double edge){
        this.edge = edge;
    }
    public double getEdge(){ return edge;}

    public void setEdge(double edge){ this.edge = edge;}

    @Override
    public double getArea(){
        return 6*Math.pow(getEdge(), 2);
    }
    @Override
    public double getVolume(){
        return Math.pow(getEdge(), 3);
    }
    @Override
    public String toString() {
        return String.format("Egde: %s%.2f\n", super.toString(), getEdge());
    }
}
