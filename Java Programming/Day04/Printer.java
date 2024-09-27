package Day04;
import Day03_StringClass.Salaried_Employee;
import java.awt.print.Book;

public class Printer {
    public void printData(Printable p){
        p.print();
    }

    public static void main(String[] args){
        Printer p = new Printer();
        A04__Book b = new A04__Book("Head First Java", 900);
        p.printData(b);

        Salaried_Employee e = new Salaried_Employee(21, "aaa", 90000);
        p.printData(e);
    }
}
