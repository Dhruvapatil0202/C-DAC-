package Day04;

public abstract class Employee{
    protected int empid;
    protected String name;

    public Employee(int empid, String name){
        this.empid = empid;
        this.name = name;
    }
    public abstract double calculateGross();

    public void print(){
        System.out.println("Employee Data: Emplyeeid = " + empid + "Name" + name);
    }
}

