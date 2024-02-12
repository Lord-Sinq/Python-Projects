/**
 * @author Sinclair DeYoung
 * @section CSC 331-003
 * @purpose driver file for shapes
 * @date 03-11-2023
 */
public class ShapeDriver {
    public static void main(String[] args){

        Shape circle = new Circle(7.4);
        Shape square = new Square(1.2);
        Shape triangle = new Triangle(2.3, 3.7);
        Shape sphere = new Sphere(2.7);
        Shape cube = new Cube(7.4);
        Shape tetrahedron = new Tetrahedron(1.8);

        Shape[] shapes = {circle, square, triangle, sphere, cube, tetrahedron};

        for (Shape currentShape : shapes){
            if(currentShape instanceof TwoDimensionalShape){
                TwoDimensionalShape twoDimensionalShape = (TwoDimensionalShape) currentShape;
                System.out.printf("Two dimensional shape: %s", currentShape.getClass().getSimpleName());
                System.out.printf("\n Area: %.2f\n\n", twoDimensionalShape.getArea());
            } else if (currentShape instanceof ThreeDimensionalShape){
                ThreeDimensionalShape threeDimensionalShape = (ThreeDimensionalShape) currentShape;
                System.out.printf("Three dimensional shape: %s", currentShape.getClass().getSimpleName());
                System.out.printf("\n Volume: %.2f\n", threeDimensionalShape.getVolume());
                System.out.printf(" Area: %.2f\n\n", threeDimensionalShape.getArea());
            }
        }
    }
}
