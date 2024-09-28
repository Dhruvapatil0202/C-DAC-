package Day05.Assignments.NewEmployee;

import java.util.Comparator;

class EmpSalComparator implements Comparator<Employee> {

    @Override
    public int compare(Employee o1, Employee o2) {
        return Double.compare(o1.getSalary(), o2.getSalary());
    }
}