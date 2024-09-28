package Day05.Assignments.AccountsAssignment;

public class Account {
    private final String name;
    private double balance;
    private int transactions;

    public Account(String name, double balance) throws IncorrectDenominationException{
        this.transactions = 3;
        this.name = name;
        this.balance = 0;
        this.deposite(balance);
    }

    public void deposite(double depositeAmount) throws IncorrectDenominationException{
        assert (depositeAmount >= 0);
        if (depositeAmount % 100 != 0){
            throw new IncorrectDenominationException(depositeAmount + " is not divisible by 100! Try again.");
        }
        else{
            this.balance += depositeAmount;
            System.out.println(this.name + " Has successfully deposited " + depositeAmount + " amount." + " Transactions limit: " + this.transactions);
        }
    }

    public void withdraw(int withdrawAmount) throws IncorrectDenominationException, InsufficientFundException, TransactionLimitExceddedException {
        assert(withdrawAmount > 0);
        if (withdrawAmount % 100 != 0){
            throw new IncorrectDenominationException(this.name + ": The withdraw amount " + withdrawAmount + " is not divisible by 100");
        } else if (withdrawAmount > this.balance){
            throw new InsufficientFundException(this.name + ": The currenct fund is " + this.balance + " and you cannot withdraw " + withdrawAmount + " credits form it.");
        } else if (this.transactions == 0) {
            throw new TransactionLimitExceddedException(this.name + ": The current Transaction Limit is Reached, Please try again after some time");
        } else {
            this.balance -= withdrawAmount;
            this.transactions -= 1;
            System.out.println(this.name + " Has successfully withdrawn " + withdrawAmount + " amount" + " Transactions limit: " + this.transactions);
        }

    }

    public static void main(String[] args) {
        try {
            Account user1 = new Account("user1", 2000);
//            System.out.println(user1.balance);
//            user1.withdraw(432);  // -> Throws denomination exception
//            user1.deposite(654);  // -> Throws denomination exception
//            user1.withdraw(1600); // -> Throws insufficient balance exception

            user1.withdraw(500);

            user1.withdraw(1000);

            user1.withdraw(100);

            user1.withdraw(100); // -> Throws transaction limit exception
        }

        catch(InsufficientFundException | IncorrectDenominationException | TransactionLimitExceddedException e){
            System.out.println(e.getMessage());
        }

    }
}
