package Day02;

public class Date_D2 {
    private int day;
    private String month;
    private int year;

    public void setDate(int d, String m, int y){
        day = d;
        month = m;
        year = y;
    }

    public Date_D2(int d, String m, int y){
        day = d;
        month = m;
        year = y;
    }

    public void displayDate(){
        System.out.println("Date: " + day + "/" + month + "/" + year);
    }

}

