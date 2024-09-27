package Day03_StringClass;

// 33-47 special chars          48-57 - numbers             65-90 uppercase        97-122 lowercase

import java.util.Arrays;

public class As02_charCounter {

    public static int[] charTypes(String str){

        int uppercase = 0;
        int lowercase = 0;
        int specialChars = 0;
        int numbers = 0;

        for(int i=0; i< str.length(); i++){

            int num = (int) str.charAt(i);
            if (33 <= num && 47 >= num) specialChars += 1;
            else if (48 <= num && 57 >= num) numbers += 1;
            else if (65 <= num && 90 >= num) uppercase += 1;
            else if (97 <= num && 122 >= num) lowercase += 1;

        }
        return new int[]{specialChars, numbers, uppercase, lowercase};

    }

    public static void main(String[] args) {

        String str = "adfbSHI23654#@!$";

        System.out.println(Arrays.toString(charTypes(str)));

    }
}
