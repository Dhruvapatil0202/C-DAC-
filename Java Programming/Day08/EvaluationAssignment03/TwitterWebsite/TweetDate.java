package Day08.EvaluationAssignment03.TwitterWebsite;

public class TweetDate {
    int day;
    int month;
    int year;

    public TweetDate(int day, int month, int year){

        this.day = day;
        this.month = month;
        this.year = year;

    }

    @Override
    public String toString() {
        return "TweetDate{" +
                "day=" + day +
                ", month=" + month +
                ", year=" + year +
                '}';
    }
}
