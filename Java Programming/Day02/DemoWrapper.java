package Day02;

public class DemoWrapper {

    public static void main(String[] args) {
        int i = 5;


        // The data cannot be inputted in collection without boxing it in wrapper.
        // The data cannot be operated on unless it has been taken out or wrapper.

        // primitive - wrapper
        // int - Integer
        // char - Character
        // float - Float
        // boolean - Boolean
        // byte - Byte
        // long - Long
        // double - Double
        // short - Short

        // Primitive to Wrapper
        Integer j = Integer.valueOf(i);
        System.out.println(j);

        // Wrapper to Primitive.
        int k = j.intValue();
        System.out.println(k);

        // Auto - boxing
        Integer x = 5;

        // Auto - unboxing
        int y = x;
        System.out.println(y);

    }
}
