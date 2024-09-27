package Day03_StringClass;

import Day04.Printable;

public class Salaried_Employee extends Employee implements Printable {
    protected double basic;

    public Salaried_Employee (int empid, String name, int basic){
        super(empid, name);
        this.basic = basic;
    }

    @Override
    public double calculateGross() {
        return this.basic + this.basic * 0.4 + this.basic * 0.12;
    }

    public double calculateNet(){
        double gross = this.calculateGross();
        double tax = gross * 0.2;
        return gross - tax;
    }

    @Override
    public void print() {

    }
}
