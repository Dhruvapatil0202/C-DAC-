package Day04;

import java.util.Objects;

public class Car {
    private String make;
    private String model;
    private int price;

    public Car(String make, String model, int price) {
        this.make = make;
        this.model = model;
        this.price = price;
    }

    @Override
    public boolean equals(Object o){
        Car other = (Car) o;
        return (this.make.equals(other.make) &&
                this.model.equals(other.model) &&
                this.price == other.price);
    }

    public int hashCode(){
        return Objects.hash(make, model, price);
    }

    @Override
    public String toString(){
        return " " + this.make + " " + this.model + " " + this.price;
    }

    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }

}
