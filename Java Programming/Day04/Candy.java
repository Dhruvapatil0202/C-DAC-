package Day04;

public class Candy extends Dessert {
    protected double quantity;

    public Candy(String name, double price, double quantity){
        super(name, price);
        this.quantity = quantity;
    }

    @Override
    protected double calculate_Price() {
        return this.quantity * this.price / 1000; // as the quantity will be in grams
    }
}
