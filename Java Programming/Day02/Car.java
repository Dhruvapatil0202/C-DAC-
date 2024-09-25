package Day02;

public class Car
{
    private String make;
    private String model;
    private NewDate_D2 purchasedate;

    public Car(String make, String model, NewDate_D2 purchasedate){
        this.make = make;
        this.model = model;
        this.purchasedate = purchasedate;
    }

    public String toString(){
        return "Car make - " + make + "\nModel - "+ model + "\nPurchase Date: " + purchasedate;
      }

    public static void main(String[] args) {
        Car car = new Car("Honda", "City", new NewDate_D2(1, "March", 2022));
        System.out.println(car);
    }



}
