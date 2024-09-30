package Day06.ClassWorkAssignment.ToyManifactComp;

public class Toy {
    private int productId;
    private double rating;
    private String name;
    private double price;
    private double age;
    private String category;
    private DateForToyClass purchaseMonthYear;
    private DateForToyClass manifactMonthyear;

    public Toy(int productId,
               double rating,
               String name,
               double price,
               double age,
               String category,
               DateForToyClass manifactMonthyear,
               DateForToyClass purchaseMonthYear){

        this.productId = productId;
        this.rating = rating;
        this.name = name;
        this.price = price;
        this.age = age;
        this.purchaseMonthYear = purchaseMonthYear;
        this.manifactMonthyear = manifactMonthyear;
        this.category = category;
    }


    @Override
    public String toString() {
        return "Toy{" + "\n" +
                "productId=" + productId + "\n" +
                ", name='" + name + '\'' + "\n" +
                ", price=" + price + "\n" +
                ", age=" + age + "\n" +
                ", category=" + category + "\n" +
                ", manifactMonthYear=" + manifactMonthyear + "\n" +
                ", purchaseMonthYear=" + purchaseMonthYear + "\n" +
                '}' + "\n\n";
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public DateForToyClass getManifactMonthyear() {
        return manifactMonthyear;
    }

    public void setManifactMonthyear(DateForToyClass manifactMonthyear) {
        this.manifactMonthyear = manifactMonthyear;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getAge() {
        return age;
    }

    public void setAge(double age) {
        this.age = age;
    }

    public DateForToyClass getPurchaseMonthYear() {
        return purchaseMonthYear;
    }

    public void setPurchaseMonthYear(DateForToyClass purchaseMonthYear) {
        this.purchaseMonthYear = purchaseMonthYear;
    }


}
