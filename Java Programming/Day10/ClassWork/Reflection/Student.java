package Day10.ClassWork.Reflection;

import Day10.ClassWork.Annotations.CreatedBy;

public class Student {
    private int rollno;
    private String name;

    public Student(){
        rollno = 100;
        name = "ppp";
    }

    public Student(int rollno, String name){
        this.rollno = rollno;
        this.name = name;
    }

    private void PrivateMethod(){
        System.out.println("This is a private method");
    }

    public static void staticMethod(){
        System.out.println("This is a static method");
    }

    @CreatedBy(priority = 1, createdBy = "aaaa")
    public void displayData(){
        System.out.println("Roll no " + rollno + " Name "+ name);
    }

    public void methodWithParam(int rollno){
        this.rollno = rollno;
        System.out.println("Roll no set to : " + rollno);
    }

}
