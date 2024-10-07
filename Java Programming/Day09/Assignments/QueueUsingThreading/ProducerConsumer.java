package Day09.Assignments.QueueUsingThreading;

public class ProducerConsumer {
    public static void main(String[] args) {

        TempQueue myQue = new TempQueue();
        Thread producer = new Thread(new Runnable() {
            @Override
            public void run(){
                for (int i = 0; i < 5; i++) {
                    myQue.setValue();
                    try { Thread.sleep(1000); } catch (InterruptedException e){e.printStackTrace();}
                }
            }
        });

        Thread consumer = new Thread(new Runnable() {
            @Override
            public void run() {
                while (!myQue.theQueue.isEmpty()){
                    myQue.getValue();
                    try { Thread.sleep(1000); } catch (InterruptedException e){e.printStackTrace();}
                }
            }
        });

        producer.start();
        consumer.start();
    }
}
