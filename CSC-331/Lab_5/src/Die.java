/**
 * @purpose this is the UML for the diceGame
 * @author Sinclair DeYoung
 * @date 29-08-2023
 * @section csc 331-003
 */
import java.util.Random;
public class Die {
    //class attributes
    private int numSides;
    private String primaryColor;
    private String secondaryColor;
    private String numColor;
    private int[] sideValues;
    //constructor
    public Die(int numSides, String primaryColor, String secondaryColor, String numColor, int[] sideValues){
        this.numSides = numSides;
        this.primaryColor = primaryColor;
        this.secondaryColor = secondaryColor;
        this.numColor = numColor;
        this.sideValues = sideValues;
    }
    //accessor methods
    public int getNumSides(){return numSides;}
    public String getPrimaryColor(){return primaryColor;}
    public String getSecondaryColor(){return secondaryColor;}
    public String getNumColor(){return numColor;}
    public int[] getSideValues(){return sideValues;}

    //mutator methods
    public void setNumSides(int numSides){ this.numSides = numSides;}
    public void setPrimaryColor(String primaryColor){ this.primaryColor = primaryColor;}
    public void setSecondaryColor(String secondaryColor){ this.secondaryColor = secondaryColor;}
    public void setNumColor(String numColor){ this.numColor = numColor;}
    public void setSideValues(int[] sideValues){ this.sideValues = sideValues;}

    // roll method
    public int roll(){
        Random rand = new Random();
        return rand.nextInt(numSides) + 1;
    }
    void displayAttributes(){
        System.out.println("Number of sides: " + numSides);
        System.out.println("Primary color: " + primaryColor);
        System.out.println("Secondary color: " + secondaryColor);
        System.out.println("Number color: " + numColor);
    }
}
