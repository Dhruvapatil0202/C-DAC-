
package Day06.ClassWork.FunctionalProgramming.StringFuncInterface;
import java.util.ArrayDeque;
import java.util.ArrayList;

public class StringManipulator {

    public static String operateOnStr(StringInterface SI, String str){
        StringBuilder outStr = new StringBuilder();
        for (Character chr : str.toCharArray()) {
            outStr.append(SI.lookFor(chr.toString()));
        }
        return outStr.toString();
    }

    public static String operateOnStrRev(StringInterface SI, String s){
        return SI.lookFor(s);
    }


    public static void main(String[] args) {
        String text = "AbcdeFGHijklmNopQRstuvWxyZ";
        StringManipulator strMan = new StringManipulator();

        String temp = strMan.operateOnStr((n) -> n.toUpperCase(), text);
        System.out.println(temp);

        String temp2 = strMan.operateOnStrRev((n) -> {
            String news = "";
            for (int i = n.length()-1; i >= 0 ; i--) {
                news += n.charAt(i);
            }
//            System.out.println("From inside lambda: " + news);
            return news;
        }, text);
        System.out.println(temp2);

        System.out.println(operateOnStr(String::toUpperCase, "Lambda"));
        System.out.println(operateOnStrRev(String::toLowerCase, "LAMbDa"));
//        String upper = operateOnStr(String::toUpperCase, "Lambda");
//        String reverse = operateOnStr(StringManipulator::operateOnStrRev, "Lambda");
//
    }

}
