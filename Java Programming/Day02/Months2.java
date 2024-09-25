package Day02;

public enum Months2 {
    JANUARY(31),
    FEBRUARY(28),
    MARCH(31),
    APRIL(30),
    MAY(31),
    JUNE(30),
    JULY(31),
    AUGUST(31),
    SEPTEMBER(30),
    OCTOBER(31),
    NOVEMBER(30),
    DECEMBER(31);

    final int days;
    Months2(int inpDays){
        this.days = inpDays;
    }
    public int getDays(){
        return days;
    }
}
