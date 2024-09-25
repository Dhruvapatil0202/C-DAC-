package Day02;

public class A04_Sorting_PassingByRef {

    public static void sort(int[] arr){

//        int ind_Count = 0;
        for (int i =0; i < arr.length-1; i++){

            for(int j = i+1; j<arr.length; j++){
                if(arr[i] > arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }

        }

        for(int i= 0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println("");
    }
    public static void main(String[] args) {


        int[] arr = {12, 3, 5, 2, 46, 23, 10};

        sort(arr);
        for(int i= 0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }

    }
}
