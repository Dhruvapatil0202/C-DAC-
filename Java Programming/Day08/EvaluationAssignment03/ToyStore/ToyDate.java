package Day08.EvaluationAssignment03.ToyStore;

public class ToyDate {

    String month;
    int year;

    public ToyDate(String month, int year){

        this.month = month;
        this.year = year;

    }


    public String toString(){
        return "Date of Manufacturing: " + month + " " + year;
    }

}

