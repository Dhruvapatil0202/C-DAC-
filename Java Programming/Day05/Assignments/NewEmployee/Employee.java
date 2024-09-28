package Day05.Assignments.NewEmployee;

import java.util.Set;

public class Employee implements Comparable<Employee>{

    private int empid;
    private String name;
    private double salary;
    private Set<String> skillset;

    public Employee(int empid, String name, double salary, Set<String> skillset) {
        this.empid = empid;
        this.name = name;
        this.salary = salary;
        this.skillset = skillset;
    }

    @Override
    public int compareTo(Employee o) {
        return this.empid - o.empid;
//        if(this.getEmpid() > o.getEmpid())
//            return 1;
//        else
//            return -1;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "empid=" + empid +
                ", name='" + name + '\'' +
                ", salary=" + salary +
                ", skillset=" + skillset +
                '}';
    }

    public void setEmpid(int empid) {
        this.empid = empid;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void setSkillset(Set<String> skillset) {
        this.skillset = skillset;
    }

    public double getSalary() {
        return salary;
    }

    public Set<String> getSkillset() {
        return skillset;
    }

    public String getName() {
        return name;
    }

    public int getEmpid() {
        return empid;
    }


}
