package Day06.ClassWork.FunctionalProgramming;

public class FPEmployee {
    String name;
    double salary;
    int Id;

    public FPEmployee(int id, String name, double salary) {
        Id = id;
        this.name = name;
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "FPEmployee{" +
                "name='" + name + '\'' +
                ", salary=" + salary +
                ", Id=" + Id +
                '}';
    }
}
