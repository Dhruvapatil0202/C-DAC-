package Day02;

public enum Flavour {

    CHOCOLATE(120), MINT(100), CREAM(90);

    final int price;
    private Flavour(int price){
        this.price = price;
    }

    public int getPrice(){
        return price;
    }

}
