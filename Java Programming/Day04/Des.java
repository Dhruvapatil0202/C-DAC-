package Day04;

public enum Des {
    COCONUT_CANDY(100, "gms", "Coconut candy"),
    STRAWBERRY_CANDY(120, "gms", "Strawberry candy"),
    MANGO_CANDY(125, "gms", "Mango candy"),
    CHOCOLATE_COOKIE(115, "no", "Chocolate cookie"),
    RESIN_COOKIE(90, "no", "Resin cookie"),
    COCONUT_COOKIE(150, "no", "Coconut cookie"),
    VANILLA_ICECREAM(100, "no", "Vanilla icecream"),
    CHOCOLATE_ICECREAM(120, "no", "Cholocate icecream"),
    BUTTER_SKOTCH(120, "no", "Butter skotch icecream");

    final double price;
    final String qty;
    final String name;

    Des(double price, String qty, String name){
        this.price = price;
        this.qty = qty;
        this.name = name;
    }

    public String getQty(){return this.qty;}
    public String getName(){return this.name;}
    public double getPrice(){return this.price;}

}
