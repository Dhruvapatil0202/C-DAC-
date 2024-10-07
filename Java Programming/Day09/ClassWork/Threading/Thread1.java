package Day09.ClassWork.Threading;

public class Thread1 extends Thread{

    /*
    -> Thread implements Runnable interface
    -> As Thread1 extends Thread, Thread1 also has an opportunity to override the
        run method.
    ->
     */
    public void run(){
        for(int i =0; i < 10; i++){
            System.out.println(Thread.currentThread().getName() + " " + i);
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
