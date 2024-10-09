package Day10.ClassAssignments.ThreadAssignment;

public class Account {
    private double balance;

    public Account(double balance) {
        this.balance = balance;
    }

    public synchronized void deposit(double amount){
        assert(amount >= 0);
        this.balance += amount;
        System.out.println("Deposited " + amount + ", Current Balance: " + balance);
        notifyAll();

    }

    public synchronized void withdraw(double amount){
//        if (this.balance < amount){
//            try{
//                wait();
//            }
//            catch(InterruptedException e){
//                e.printStackTrace();
//            }
//        }
        while(this.balance < amount) {
            try {wait();} catch(InterruptedException e){
                Thread.currentThread().interrupt(); // restore interrupted state.
                e.printStackTrace();
            }
        }
        this.balance -= amount;
        System.out.println("Withdrawn " + amount + ", Current Balance: " + balance);
        notify();
    }

    public synchronized double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}
