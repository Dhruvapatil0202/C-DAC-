package Day06.ClassWorkAssignment.ToyManifactComp;

public class DateForToyClass {
    public String month;
    public int year;

    public DateForToyClass(String month, int year) {
        this.month = month;
        this.year = year;
    }

    @Override
    public String toString() {
        return "DateForToyClass{" +
                "month='" + month + '\'' +
                ", year=" + year +
                '}';
    }
}

