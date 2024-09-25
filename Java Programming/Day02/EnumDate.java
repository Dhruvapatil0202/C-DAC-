package Day02;

public class EnumDate {
    Months2 month;
    private int day;
    private int year;

    public void setDate(int d, Months2 m, int y){
        day = d;
        month = m;
        year = y;
    }

    public EnumDate(int d, Months2 m, int y){
        day = d;
        month = m;
        year = y;
    }

    public void displayDate(){
        System.out.println("Date: " + day + "-" + month + "-" + year);
    }

    public String toString(){
        return "Date: " + day + "-" + month + "-" + year;
    }


    public static void main(String[] args) {
        EnumDate abc = new EnumDate(4, Months2.JANUARY, 2024);
        System.out.println(abc);
    }

}
