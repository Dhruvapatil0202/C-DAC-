package Day01;

public class Account {
    private int accid;
    private String name;
    private static float int_rate;

    static{
        System.out.println("Static block 1");
    }

    static{
        System.out.println("Static block 2");
    }

    public static void display_Interest_Rate(){
        System.out.println("Interest_rate: " + int_rate);
    }

    public Account(int accid, String name){
        this.accid = accid;
        this.name = name;
    }

    public static void main(String[] args) {
        System.out.println("Current interest rate for account : " + int_rate);
    }
}
