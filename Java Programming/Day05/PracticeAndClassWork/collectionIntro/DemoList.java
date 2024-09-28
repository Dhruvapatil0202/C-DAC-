package Day05.PracticeAndClassWork.collectionIntro;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class DemoList {
    public static void main(String[] args) {
        List lst = new ArrayList<>();

        // List is unhomogeneous ordered list (can accomodate data of variable datatyes)

        lst.add(120);
        lst.add("Test");
        lst.add(24.5655);
        lst.add(true);

//        for(Object ele: lst){
//            System.out.println(ele + " " + ele.getClass());
//        }
        for (int ele = 0; ele < lst.size(); ele++) {
            System.out.println(lst.get(ele));
        }

        lst.remove(24.5655);

        for(Object ele: lst){
            System.out.println(ele + " " + ele.getClass());
        }

        for (Object o : lst) {
            System.out.println(o);
        }

        for (Object obj : lst) {
            int i = (Integer)obj;
            System.out.println(i++);
        }

    }
}
