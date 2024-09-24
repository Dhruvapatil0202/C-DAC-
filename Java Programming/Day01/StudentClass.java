package Day01;

public class StudentClass {

    public class Student{

        private String name;
        private String gender;
        private int rollNo;
        private static int rollCount = 0;

        public String toString(){
            return "\nName: " + name + "\nGender: " + gender + "\nRollNo: " + rollNo + "\n";
        }

        public Student(String Name, String Gender){
            name = Name;
            gender = Gender;
            rollNo = rollCount + 1;
            rollCount += 1;
        }

    }

    public static void main(String[] args) {

        StudentClass Class1 = new StudentClass();
        Student stud1 = Class1.new Student("Name1", "Male");
        Student stud2 = Class1.new Student("Name2", "Male");
        Student stud3 = Class1.new Student("Name3", "Female");
//        System.out.println("Hello");

        System.out.println(stud1);
        System.out.println(stud2);
        System.out.println(stud3);

        System.out.println("The total number of students are: " + Student.rollCount);

    }
}
