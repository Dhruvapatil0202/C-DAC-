package Day04;

public interface Printable {
    void print();
    default void foo(){
        System.out.println("This is default functionality");
    }
}
