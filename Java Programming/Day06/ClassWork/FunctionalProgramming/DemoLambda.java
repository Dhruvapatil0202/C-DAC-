package Day06.ClassWork.FunctionalProgramming;

public class DemoLambda {
    public static void main(String[] args) {
        Predicate isEven = (n) -> n % 2 == 0;
        System.out.println(isEven.test(13));
        System.out.println(isEven.test(24));

        Predicate isPrime = (n) -> {
            for (int i = 2; i < n; i++) {
                if (n % i == 0) return false;
            }
            return true;
        };
        System.out.println(isPrime.test(25));
    }
}
