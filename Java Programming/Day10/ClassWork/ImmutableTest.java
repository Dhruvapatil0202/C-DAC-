package Day10.ClassWork;

import java.time.LocalDate;
import java.util.ArrayList;

public class ImmutableTest {
    public static void main(String[] args) {
        ArrayList<String> colors = new ArrayList<>();
        colors.add("White");
        colors.add("Black");

        LocalDate mdate = LocalDate.of(2020, 12, 10);
        ImmutableClass c = new ImmutableClass("aaa", "bbb", mdate, colors);

        System.out.println(c);
        colors.add("Red");
        System.out.println(c.getColors());
        System.out.println(colors);

    }
}
