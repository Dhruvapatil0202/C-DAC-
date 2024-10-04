package Day07.Classwork.NewEmployeeApp;

import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class EmployeeStream {
    public List<Employee> initializeData(){
        List<Employee> empList = new ArrayList<>();

        Set<String> st1 = new TreeSet<>();
        st1.add("cpp");
        st1.add("java");
        empList.add(new Employee(111, "IT", st1 , 76000, "aaa"));

        Set<String> st2 = new TreeSet<>();
        st2.add("cpp");
        st2.add("python");
        empList.add(new Employee(222, "IT",  st2 , 57000, "qqq"));

        Set<String> st3 = new TreeSet<>();
        st3.add("python");
        st3.add("java");

        empList.add(new Employee(333, "Admin", st3 , 120000,"ppp"));
        Set<String> st4 = new TreeSet<>();
        st4.add("javaScript");
        st4.add("go");
        empList.add(new Employee(444,"Admin", st4 , 80000, "ttt"));

        return empList;
    }

    public static void main(String[] args) {
        EmployeeStream e = new EmployeeStream();
        List<Employee> emplist = e.initializeData();
        Stream<Employee> stream = emplist.stream();

        Comparator<Employee> byname = Comparator.comparing(Employee::getName);
        System.out.println("_____sorting by name_____");
        stream.sorted(byname).forEach(System.out::println);

        stream = emplist.stream();
        Comparator<Employee> bydept = Comparator.comparing(Employee::getDepartment).thenComparing(byname);
        stream.sorted(bydept).forEach(System.out::println);

        System.out.println("_________________________");
        stream = emplist.stream();
        Predicate<Employee> empSalRange = (emp) -> (emp.getSalary() > 50000 && emp.getSalary() < 70000);


        System.out.println("_______filter by skill_____________");
        stream = emplist.stream();
        stream.filter((emp) -> emp.getSkillset().contains("Java")).forEach(System.out::println);

        System.out.println("____________group by department_____________");
        stream = emplist.stream();
        Map<String, List<Employee>> empsbydept = stream.collect(Collectors.groupingBy(Employee::getDepartment));

        empsbydept.forEach((k, v) -> System.out.println(k + "_____" + v));

        System.out.println("__________________");
        stream = emplist.stream();
        stream.map((emp) -> new Department(emp.getEmpid(), emp.getDepartment()));

        System.out.println("____________________________");
        stream = emplist.stream();
        double totalsal = stream.mapToDouble(Employee::getSalary).reduce(0, (e1, e2) -> e1 + e2);
        System.out.println(totalsal);

    }
}
