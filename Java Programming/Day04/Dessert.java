package Day04;

public abstract class Dessert {

    protected String name;
    protected double price;

    protected abstract double calculate_Price();

    public String get_stat(){
        return name + "________" + calculate_Price();
    }

    public Dessert(String name, double price){
        this.name = name;
        this.price = price;
    }

}
