package Day03_StringClass;

public abstract class Employee {

    protected int empid;
    protected String name;

    public Employee(int empid, String name){
        this.empid = empid;
        this.name = name;
    }

    public abstract double calculateGross();

    public String toString(){
        return "Employee Data: Employee id - " + empid + " , Name - " + name;
    }
}
