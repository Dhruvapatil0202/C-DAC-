package Day10.ClassWork;

import java.lang.reflect.Array;

public class DemoArray {
    public static void main(String[] args) {
        String [] arr = (String[]) Array.newInstance(String.class, 3);

        Array.set(arr, 0, "a");
        Array.set(arr, 1, "b");
        Array.set(arr, 2, "c");

        for (String s : arr) {
            System.out.println(s);
        }
    }
}
