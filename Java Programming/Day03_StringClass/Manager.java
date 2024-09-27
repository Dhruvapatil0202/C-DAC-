package Day03_StringClass;

public class Manager extends Salaried_Employee {

    protected double allowance;

    public Manager(int empid, String name, int basic, double allowance){
        super(empid, name, basic);
        this.allowance = allowance;
    }

    @Override
    public double calculateGross(){
        return super.calculateGross() + this.allowance;
    }

    public void displayAllowance(){
        System.out.println("Allowance: " + this.allowance);
    }

}
