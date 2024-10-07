package Day09.ClassWork.Threading;

public class DemoSynchronization {

    public static void main(String[] args) {

        Counter count = new Counter();

        new Thread(new Runnable(){
            public void run(){
                synchronized (count) {
                    for (int i = 0; i < 50; i++) {
                        count.increment();
                        System.out.println(Thread.currentThread().getName() + ":" + count.getCount());
                        try {
                            Thread.sleep(500);
                        } catch (InterruptedException e){
                            e.printStackTrace();
                        }
                    }
                }
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (count) {
                    for (int i = 0; i < 50; i++) {
                        count.increment();
                        System.out.println(Thread.currentThread().getName() + ":" + count.getCount());
                    }
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();

    }

}
