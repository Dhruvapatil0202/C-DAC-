package Day04;

public class Ice_Cream extends Dessert{

    protected int quantity;
    public Ice_Cream(String name, double price, int quantity){
        super(name, price);
        this.quantity = quantity;
    }

    @Override
    protected double calculate_Price() {
        return this.price * this.quantity; // quantity will be the number of icecream cups.
    }
}
