package Day10.ClassAssignments.ThreadAssignment;

public class CodeDriver {

    public static void main(String[] args) {
        Account acc = new Account(10000);

        Thread withdraw1 = new Thread(() -> {
            for (int itr = 0; itr < 3; itr++) {
                acc.withdraw(6000);
                try{Thread.sleep(2000);} catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        });
        withdraw1.setName("Withdraw1");



//        Thread deposite = new Thread(new Runnable(){
//            @Override
//            public void run(){
//                for (int itr = 0; itr < 3; itr++) {
//                    acc.deposite(4000);
//                    System.out.println("deposite has deposited " + 4000 + " Money, Current balance: " + acc.getBalance());
//                    try {
//                        Thread.sleep(2000);
//                    } catch (InterruptedException e) {
//                        e.printStackTrace();
//                    }
//
//                }
//            }
//        });

        Thread deposite = new Thread(() -> {
            for (int itr = 0; itr < 3; itr++) {
                acc.deposit(4000);
                try{ Thread.sleep(2000);} catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        });
        deposite.setName("deposite");

        withdraw1.start();
        deposite.start();

    }
}
