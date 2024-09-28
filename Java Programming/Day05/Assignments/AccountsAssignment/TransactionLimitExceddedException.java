package Day05.Assignments.AccountsAssignment;

public class TransactionLimitExceddedException extends RuntimeException {
    public TransactionLimitExceddedException(String message) {

        super(message);
    }
}
