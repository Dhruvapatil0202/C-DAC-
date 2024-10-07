package Day09.ClassWork.Threading;

public class DemoThread {
    public static void main(String[] args) throws InterruptedException {

        Thread1 t1 = new Thread1();
        t1.start();

        // The Thread constructor takes object of a class which implements
        // Runnable interface directly or indirectly
        Thread t2 = new Thread(new Thread2());
        t2.start();

        for(int i=0; i<10; i++){
            System.out.println("Main Thread " + i);

            try{
                Thread.sleep(2000);
            }
            catch (InterruptedException e){
                e.printStackTrace();
            }
        }


    }
}
