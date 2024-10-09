package Day10.ClassWork.Annotations;

public class Student {
    private int rollNo;
    private String name;

    public Student(int rollno, String name){
        this.rollNo = rollno;
        this.name = name;
    }

    @CreatedBy(priority = 1, createdBy = "aaaa")
    public void displayData(){

    }
}
