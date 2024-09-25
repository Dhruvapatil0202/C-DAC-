package Day02;

import Day01.Date;

public class A02_DemoArray {
    public static void main(String[] args) {

        // First class objects can be created without using new keyword.

        int[] arr = {12, 23, 24, 25, 26};
        int arr2 [] = {22, 22, 33, 33, 44};
        for(int i : arr2){
            if(i % 2 == 0) System.out.println("Number is even");
            else System.out.println("Number is odd");
        }

        Date[] dates = new Date[3];
        for(int dateInd = 0; dateInd < dates.length; dateInd++){
            dates[dateInd] = new Date();
            dates[dateInd].setDate(dateInd + 11, "Aug", 2024);
            dates[dateInd].displayDate();
        }
    }
}
