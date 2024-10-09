package Day10.ClassWork.Reflection;

import java.lang.reflect.*;
import java.util.Arrays;

public class CodeDriver {
    public static void main(String[] args) throws IllegalAccessException, NoSuchMethodException, InvocationTargetException, InstantiationException {
        Student s =  new Student();
        Class c = s.getClass();

        Field[] field = c.getDeclaredFields();
        for (Field f : field) {
            System.out.println(f.getName());
            System.out.println(f.getType());
            if(f.getName().equals("rollno")){
                f.setAccessible(true);
                f.setInt(s, 110);
            }

            if(f.getName().equals("name")){
                f.setAccessible(true);
                f.set(s, "nnn");
            }
        }
        s.displayData();

        Constructor[] cons = c.getDeclaredConstructors();
        for (Constructor con : cons){
            System.out.println(Arrays.deepToString(con.getParameterAnnotations()));
            if (con.getParameterAnnotations().length == 2){
                Parameter[] params = con.getParameters();
                System.out.println(Arrays.toString(params));
                Student s1 = (Student) con.newInstance(111, "Hmmm");
                s1.displayData();
            }
        }

        Method[] methods = c.getDeclaredMethods();
        for(Method m : methods) {
            System.out.println(m.getName());
            if (m.getName().equals("privateMethod")){
                m.setAccessible(true);
                m.invoke(s);
            }

            if (m.getName().equals("staticMethod")){
                m.setAccessible(true);
                m.invoke(null);
            }

            if (m.getName().equals("methodWithParameter")){
                Parameter[] parameters = m.getParameters();
                System.out.println(Arrays.toString(parameters));
                m.invoke(s, 456, "KKK");
            }
        }

        for(Method m: methods){
            if (true){

            }
        }
    }
}
