package Day04;

import Day04.Printable;

public class SalariedEmployee implements Printable {
    protected double basic;
    protected String name;
    protected int empid;

    public SalariedEmployee (int empid, String name, int basic){
        this.empid = empid;
        this.basic = basic;
        this.name = name;
    }

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
        System.out.println("\nName: " + name + "\nempid: " + empid);
    }
}