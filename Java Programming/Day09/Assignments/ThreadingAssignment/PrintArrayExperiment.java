package Day09.Assignments.ThreadingAssignment;

interface ArrayPrinter extends Runnable{
    @Override
    public void run();
}

public class PrintArrayExperiment {


    public static void main(String[] args) {
        char[] charArray = {'G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g'};

        Runnable t = () -> {
            synchronized(charArray){
                for(char chr : charArray) System.out.print(chr);
                System.out.println();
            }
        };

        Thread temp = new Thread(new Runnable(){
            @Override
            public void run(){

            }
        });

        Thread thread1 = new Thread(t);
        Thread thread2 = new Thread(t);

        thread1.start();
        thread2.start();
    }
}

