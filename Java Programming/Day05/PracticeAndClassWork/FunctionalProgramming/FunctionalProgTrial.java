package Day05.PracticeAndClassWork.FunctionalProgramming;

public class FunctionalProgTrial {
    public static void main(String[] args) {

        Runnable func = () -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Hello From Turead!" + i);
            }
        };

        Thread thread = new Thread(func);
        thread.start();
    }
}
