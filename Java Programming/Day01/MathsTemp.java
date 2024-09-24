package Day01;

public class MathsTemp {

    public static int factorial(int limit){

        int out = 1;
        for(int num = 1; num <= limit; num++){
            out *= num;
        }
        System.out.println(out);
        return out;
    }

    public static void isPrime(int num){

        for(int i = 2; i < (int)Math.sqrt(num); i++){
            if (num % i == 0){
                System.out.println(num + " is Not Prime");
                return;
            }
        }
        System.out.println(num + " is Prime");
        return;
    }

    public static int add(int v1, int v2){
        return v1 + v2;
    }
    public static int add(int v1, int v2, int v3){
        return v1 + v2 + v3;
    }
    public static float add(int v1, float v2){
        return v1 + v2;
    }
    public static float add(float v1, int v2){
        return v1 + v2;
    }


    // int...num is variable argument
    //variable argument is last argument in declaration
    //Only one variable argument is used.
    // Variable argument is dynamic array
    public static int add(int...num){
        int out = 0;
        for(int i : num) out += i;
        return out;
    }

    public static void main(String[] args) {
        String s = args[0];
        String s1 = args[1];
        System.out.println( s + " " + s1);
        MathsTemp.isPrime(17);

        // function overloading
//        System.out.println(MathsTemp.add(1, 3.5f) +" " + MathsTemp.add(1, 3, 5) + " " +MathsTemp.add(3, 4) + " " + MathsTemp.add(2.5f, 6));

        // Function with variable number of arguments.
        System.out.println(MathsTemp.add(10, 20, 30, 40, 50));


    }
}
