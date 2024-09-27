package Day04;

public class Cookies extends Dessert{
    protected int quantity;

    public Cookies(String name, double price, int quantity){
        super(name, price);
        this.quantity = quantity;
    }

    @Override
    protected double calculate_Price() {
        return this.quantity * this.price / 12; // as the quantity will be the number of cookies
    }

}
