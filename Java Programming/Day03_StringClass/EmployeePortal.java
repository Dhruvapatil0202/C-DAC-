package Day03_StringClass;

public class EmployeePortal {
    public static void main(String[] args) {
        Payroll payroll = new Payroll();

        Salaried_Employee se = new Salaried_Employee(234, "aaa", 80000);
        payroll.displayGross(se);
        payroll.displayNet(se);

        Employee[] emps = new Employee[2];
        emps[0] = new Salaried_Employee(667, "ppp", 50000);
        emps[1] = new Salaried_Employee(668, "qqq", 10000);

        /*
        calculate Gross() is defined in e plooyee and overridden in Salaried Employee
        hence be invoked using Employeee referance emps[0]
         */

        payroll.displayGross(emps[0]);

        /*
        To invoke CcaculateNet() which is defined in SalaridEmployee
        the Employee reference must be down caste to SalariedEmployee
         */
        Salaried_Employee ss = (Salaried_Employee)emps[0]; // Downcasting
        payroll.displayNet(ss);

        for(Employee e : emps){
            payroll.displayGross(e);
            if(e instanceof Manager)
                ((Manager)e).displayAllowance();
        }
    }
}
