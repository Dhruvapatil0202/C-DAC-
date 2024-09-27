package Day03_StringClass;

public class Contract_Employee extends Employee {
    protected double rate;
    protected double hours;

    public Contract_Employee(int empid, String name, double rate, double hours){
        super(empid, name);
        this.rate = rate;
        this.hours = hours;
    }

    @Override
    public double calculateGross(){
        return this.rate * this.hours;
    }

}
