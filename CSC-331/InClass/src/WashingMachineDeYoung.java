public class WashingMachineDeYoung {
    public String brand;
    public String model;
    public double price;
    public WashingMachineDeYoung(String brand, String model, double price){
        this.brand = brand;
        this.model = model;
        this.price = price;
    }
    public String getBrand(){ return brand;}
    public String getModel(){ return model;}
    public double getPrice(){ return price;}

    private void setBrand(String brand){this.brand = brand;}
    private void setModel(String model){this.model = model;}
    private void setPrice(double price){this.price = price;}

    public double salePrice(){ return price * 0.95;}

}
