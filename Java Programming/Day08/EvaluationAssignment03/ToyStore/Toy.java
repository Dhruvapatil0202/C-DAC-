package Day08.EvaluationAssignment03.ToyStore;

public class Toy {
    private int productId;
    private String name;
    private double price;
    private double ageLimit;
    private String category;
    private ToyDate mfgDate;
    private ToyDate purchaseDate;

    public Toy(int productId, String name, double price, String category, double age, ToyDate mfgDate, ToyDate purchaseDate){

        this.productId = productId;
        this.name = name;
        this.price = price;
        this.category = category;
        this.ageLimit = age;
        this.mfgDate = mfgDate;
        this.purchaseDate = purchaseDate;

    }

    @Override
    public String toString() {
        return "Toy{" +
                "productId=" + productId +
                ", name='" + name + '\'' +
                ", price=" + price +
                ", ageLimit=" + ageLimit +
                ", category='" + category + '\'' +
                ", mfgDate=" + mfgDate +
                ", purchaseDate=" + purchaseDate +
                '}';
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

    public void setPrice(int price) {
        this.price = price;
    }

    public double getAgeLimit() {
        return ageLimit;
    }

    public void setAgeLimit(int ageLimit) {
        this.ageLimit = ageLimit;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public ToyDate getPurchaseDate() {
        return purchaseDate;
    }

    public void setPurchaseDate(ToyDate purchaseDate) {
        this.purchaseDate = purchaseDate;
    }

    public ToyDate getMfgDate() {
        return mfgDate;
    }

    public void setMfgDate(ToyDate mfgDate) {
        this.mfgDate = mfgDate;
    }
}
