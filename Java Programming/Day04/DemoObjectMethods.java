package Day04;

public class DemoObjectMethods {
    public static void main(String[] args) {

        Car car1 = new Car("abc", "xyz", 200);
        Car car2 = new Car("abc", "xyz", 200);

        System.out.println(car1.equals(car2));
    }
}
