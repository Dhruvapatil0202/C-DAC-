package Day07.Classwork.NewEmployeeApp;

import java.util.Set;

public class Employee {
    private int empid;
    private String name;
    private double salary;
    private Set<String> skillset;
    private String department;

    public Employee(int empid, String department, Set<String> skillset, double salary, String name) {
        this.empid = empid;
        this.department = department;
        this.skillset = skillset;
        this.salary = salary;
        this.name = name;
    }

    @Override
    public String toString() {
        return "Employee{" + "\n" +
                "empid=" + empid + "\n" +
                ", name='" + name + '\'' + "\n" +
                ", salary=" + salary + "\n" +
                ", skillset=" + skillset + "\n" +
                ", department='" + department + '\'' + "\n" +
                '}';
    }

    public Set<String> getSkillset() {
        return skillset;
    }

    public void setSkillset(Set<String> skillset) {
        this.skillset = skillset;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getEmpid() {
        return empid;
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}
