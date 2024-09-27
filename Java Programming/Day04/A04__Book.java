package Day04;

public class A04__Book implements Writable, Printable{
    private String title;
    private int price;

    public A04__Book(String Title, int price){
        super();
        this.title = Title;
        this.price = price;

    }
    @Override
    public void write(){
        System.out.println("Wriging the boook");
    }

    @Override
    public void print(){
            System.out.println("Printing a book");
    }

    @Override
    public void foo(){
        Printable.super.foo();
    }
}


