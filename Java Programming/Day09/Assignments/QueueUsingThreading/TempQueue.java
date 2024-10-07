package Day09.Assignments.QueueUsingThreading;

import java.util.ArrayDeque;
import java.util.Queue;

public class TempQueue {
    ArrayDeque<Integer> theQueue = new ArrayDeque<Integer>();
    int currCnt = 1;
    int setCounter = 1;
    int getCounter = 1;

    public synchronized void setValue(){
        if (theQueue.size() == 5){
            try{ wait();}
            catch(InterruptedException e){ e.printStackTrace(); }
        }

        while(theQueue.size() < 5){
            theQueue.addLast(currCnt);
            System.out.println("Set Value : " + currCnt + " set counter " + setCounter + "\n");
            currCnt++;
            setCounter += 1;
        }

        notify();

    }

    public synchronized void getValue(){
        if(theQueue.isEmpty()){
            try{ wait(); } catch(InterruptedException e) { e.printStackTrace(); }
        }

        int outval = theQueue.getLast();
        theQueue.removeLast();
        System.out.println("Get Value : " + outval + " get counter " + getCounter+ "\n");
        getCounter += 1;

        notify();
    }
}
