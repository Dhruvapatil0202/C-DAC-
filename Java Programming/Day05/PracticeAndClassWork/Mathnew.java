package Day05.PracticeAndClassWork;

public class Mathnew {

    public static void divide(String s1, String s2) throws ArithmeticException, NumberFormatException, ArrayIndexOutOfBoundsException{

        int dividend = Integer.parseInt(s1);
        int divisor = Integer.parseInt(s2);

        int res = dividend/divisor;
        System.out.println(res);
    }

    public static void main(String[] args) {
        try{
            divide(args[0],args[1]);
        }

        // multi catch block
        catch (ArrayIndexOutOfBoundsException | ArithmeticException | NumberFormatException e){
            System.out.println("Error occured");
        }
    }
}

