package Day05.Assignments.NewEmployee;

import com.sun.source.tree.Tree;

import java.util.*;


public class EmployeeCollection {

    public List<Employee> initializeEmployeeData(){
        List<Employee> empList = new ArrayList<>();

        Set<String> st1 = new TreeSet<>();
        st1.add("cpp");
        st1.add("java");
        empList.add(new Employee(111, "aaa", 76000, st1));

        Set<String> st2 = new TreeSet<>();
        st2.add("cpp");
        st2.add("python");
        empList.add(new Employee(222, "qqq", 57000, st2));

        Set<String> st3 = new TreeSet<>();
        st3.add("python");
        st3.add("java");
        empList.add(new Employee(333, "ppp", 120000, st3));

        Set<String> st4 = new TreeSet<>();
        st4.add("javaScript");
        st4.add("go");
        empList.add(new Employee(444, "ttt", 80000, st4));

        return empList;
    }

    public void printList(List<Employee> empList){
        for (Employee employee : empList) {
            System.out.println(employee);
        }
    }

    public Employee searchEmployee(List<Employee> empList, int targetEmpId){
        for (Employee employee : empList) {
            if (employee.getEmpid() == targetEmpId)
                return employee;
        }
        return null;

    }



    public List<Employee> filterEmployees(List<Employee> emplist, String cirteria){
        List<Employee> filtered = new ArrayList<>();
        for (Employee e: emplist){
            if(e.getSkillset().contains(cirteria))
                filtered.add(e);
        }
        return filtered;
    }

    public Map<Integer, Double> salaryMap(List<Employee> emplist){
        Map<Integer, Double> salmap = new TreeMap<>();
        for(Employee e : emplist){
            salmap.put(e.getEmpid(), e.getSalary());
        }
        return salmap;
    }

    public static void main(String[] args) {

        EmployeeCollection e = new EmployeeCollection();
        List<Employee> empList = e.initializeEmployeeData();

        System.out.println("\n\t_________printing___________");
        e.printList(empList);

        System.out.println("\n\t_________Searching_________");
        System.out.println(e.searchEmployee(empList, 333));

        System.out.println("\n\t_________sorting empsal__________");
        empList.sort(new EmpSalComparator());
        e.printList(empList);

        System.out.println("\n\t_________sorting name__________");
        empList.sort(new EmpNameComparator());
        e.printList(empList);
        int index = Collections.binarySearch(empList, new Employee(0,"ppp", 0 , null), new EmpNameComparator());
        System.out.println(index);


        System.out.println("\n\t_________sorting empid__________");
        Collections.sort(empList);
        e.printList(empList);
        index = Collections.binarySearch(empList, new Employee(111,null, 0 , null));
        System.out.println(index);



        System.out.println("\n\t_________filtering_____________");
        e.printList(e.filterEmployees(empList, "python"));

        System.out.println("\n\t--------mapping--------");
        Map<Integer, Double> salemplst = e.salaryMap(empList);
        for(Map.Entry<Integer, Double> entry: salemplst.entrySet()){
            System.out.println(entry.getKey() + " ----------> " + entry.getValue());
        }

        System.out.println("\n\tMinimum Salary");
        System.out.println(Collections.min(empList, new EmpSalComparator()));

        System.out.println("\n\tMaximum Salary");
        System.out.println(Collections.max(empList, new EmpSalComparator()));

        System.out.println("\n\tReversal");
        Collections.reverse(empList);
        e.printList(empList);







//        TreeSet<String> temp = Set.of

    }
}
