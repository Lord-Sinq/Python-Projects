public class WMDriver {
	public static void main(String[] args) {
		WashingMachine[] wm = new WashingMachine[3];
		wm[0]= new WashingMachine("Whirlpool", "WTW5057L", 629);
		wm[1] = new WashingMachine("LG", "WM4000H", 849);
		wm[2] = new WashingMachine("GE", "GFW850", 1048);
		
		System.out.printf("%-15s%-15s%-15s%-15s%n", "Brand", "Model", "Price", "Sale Price");
		
		for (int i = 0; i < wm.length; i++) {
			System.out.printf("%-15s%-15s%-,15.2f%-,15.2f%n", wm[i].getBrand(), wm[i].getModel(), wm[i].getPrice(), wm[i].salePrice());	
		}
		
		System.out.println();
		
		for (WashingMachine machine : wm) {
			System.out.printf("%-15s%-15s%-,15.2f%-,15.2f%n", machine.getBrand(), machine.getModel(), machine.getPrice(), machine.salePrice());	

		}
	}
}
