package Day03_StringClass;

// Day 4

public class Payroll {
    public void displayGross(Employee e){
        System.out.println("Gross Salary: " + e.calculateGross());

    }

    public void displayNet(Salaried_Employee e){
        System.out.println("Net Salary: " + e.calculateNet());
    }
}
