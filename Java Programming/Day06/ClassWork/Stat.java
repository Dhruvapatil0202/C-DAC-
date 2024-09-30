package Day06.ClassWork;

// Generic Class

public class Stat <T extends Number> {

    T [] num;

    public void setValues(T[] num){
        this.num = num;
    }

    public double getAverage(){
        double sum = 0.0;
        for(int i=0; i < num.length; i++){
            sum += num[i].doubleValue();
        }

        return sum/ num.length;

    }

    public static void main(String[] args) {
        Integer [] arr = {12,14,26,76,89,97};
        Stat<Integer> stat1 = new Stat<>();
        stat1.setValues(arr);
        System.out.println(stat1.getAverage());

        Double [] arr2 = {12.04,14.5,26.2,76.9,89.1,97.5};
        Stat<Double> stat2 = new Stat<>();
        stat2.setValues(arr2);
        System.out.println(stat2.getAverage());



    }


}
