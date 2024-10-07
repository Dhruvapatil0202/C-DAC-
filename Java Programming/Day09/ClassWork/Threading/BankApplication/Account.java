package Day09.ClassWork.Threading.BankApplication;

public class Account {

    private double balance;

    public Account(double balance) {
        super();
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void withdraw(int amount)
    {
        balance -= amount;
    }

}
