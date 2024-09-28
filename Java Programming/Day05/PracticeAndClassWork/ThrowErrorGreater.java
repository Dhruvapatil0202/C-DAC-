package Day05.PracticeAndClassWork;

import java.io.IOException;
import java.util.Scanner;

public class ThrowErrorGreater {

    public void numberCheck(int num) throws IOException {
        if (num>60000)
        {
            throw new IOException("Number has to be less than 60000");
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        ThrowErrorGreater obj = new ThrowErrorGreater();
        try{
            obj.numberCheck(num);
        }
        catch (IOException e){
            System.out.println("Number is greater than 60000");
            System.out.println(e);
        }

    }
}
