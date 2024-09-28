package Day05.PracticeAndClassWork.collectionIntro;

//import java.util.HashSet;
import java.util.HashSet;
import java.util.Set;
//import java.util.Set;

public class DemoSet {
    public static void main(String[] args) {
        Set<Integer> st = new HashSet<>();

        st.add(12);
        st.add(22);
        st.add(13);
        st.add(15);
        st.add(16);

        for (Integer ele : st) {
            System.out.println(ele);
        }

        st.remove(22);

        System.out.println(st.contains(13));

        System.out.println(st);
    }
}
