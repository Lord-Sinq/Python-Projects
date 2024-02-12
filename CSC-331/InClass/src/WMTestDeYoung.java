public class WMTestDeYoung {
    public static void main(String[] args){
        WashingMachineDeYoung machine1 = new WashingMachineDeYoung("Samsung  ", "Y", 999.99);
        WashingMachineDeYoung machine2 = new WashingMachineDeYoung("LG      ", "q", 579.99);
        WashingMachineDeYoung machine3 = new WashingMachineDeYoung("whirlpool", "22", 599.99);

        WashingMachineDeYoung[] machines = {machine1, machine2, machine3};

        System.out.println("Brand\tModel\tSale Price");
        for (WashingMachineDeYoung machine : machines){
            System.out.printf("%s\t%2s\t%6.2f%n", machine.getBrand(), machine.getModel(), machine.price, machine.salePrice());
        }
    }
}
