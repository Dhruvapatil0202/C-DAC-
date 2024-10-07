package Day09.Assignments.ThreadingAssignment;


public class PrintArray {
    public static void main(String[] args) {
        char[] charArray = {'G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g'};

        Runnable t = () -> {
            synchronized(charArray){
                for(char chr : charArray) System.out.print(chr);
                System.out.println();
            }
        };

        Thread thread1 = new Thread(t);
        Thread thread2 = new Thread(t);

        thread1.start();
        thread2.start();
    }
}
