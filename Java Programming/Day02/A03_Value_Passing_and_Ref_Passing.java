package Day02;

//import Day02.NewDate_D2;
//import Day02.Date_D2;

import java.util.Arrays;

public class A03_Value_Passing_and_Ref_Passing {
    public static int increment(int num){
        num += 1;
        return num;
    }

    public static void increment_Date(NewDate_D2 d){
        int day = d.getDay();
        d.setDay(day + 1);
    }

    public static void swapDates(Date_D2 d1, Date_D2 d2){
        Date_D2 temp = d1;
        d1 = d2;
        d2 = temp;
    }

    public static void sortArray(int[] arr){
        int n = arr.length;
        for (int i = 0; i < n-1; i++){
            for (int j = i + 1; j < n; j++){
                if (arr[i] > arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {

        int n = 10;
        System.out.println("Before Increment: " + n);
        n = increment(n);
        System.out.println("After Increment: " + n);

        NewDate_D2 d = new NewDate_D2();
        d.setDay(12);
        d.setMonth("Jan");
        d.setYear(2034);

        System.out.println("Before Increment: " + d);
        increment_Date(d);
        System.out.println("After Increment: ");

        Date_D2 dt1 = new Date_D2(4, "Dec", 2024);
        Date_D2 dt2 = new Date_D2(5, "Dec", 2024);

        System.out.println("Before Swap: d1: " + dt1 + " d2 " + dt2);
        swapDates(dt1, dt2);
        System.out.println("After Swap: d1: " + dt1 + " d2 " + dt2);

        int[] arr = {12, 23, 5, 2, 11};
        sortArray(arr);
        System.out.println("After Sorting: " + Arrays.toString(arr));


    }

}
