package Day01;

public class NewDate {
    private int day;
    private String month;
    private int year;

    public void setDay(int day){
        if((day > 31) || (day < 1)) {
            System.out.println("Invalid date");
        }
        this.day = day;
    }

    public void setMonth(String month){
        this.month = month;
    }

    public void setYear(int year){
        this.year = year;
    }

    public int getDay(){
        return day;
    }

    public String getMonth(){
        return month;
    }

    public int getYear(){
        return year;
    }

    public String toString(){
        return day + "/" + month + "/" + year;
    }

    public NewDate(){
        this.day = 14;
        this.month = "Jan";
        this.year = 2024;
    }

    public static void main(String[] args) {
        NewDate block = new NewDate();

        System.out.println(block);

        System.out.println( block.getDay() + " " + block.getMonth() + " " + block.getYear() );

        block.setDay(7);
        block.setMonth("Dec");
        block.setYear(2004);

        System.out.println(block);

        System.out.println(block.day);
        System.out.println(block);
    }

}
