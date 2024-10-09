package Day10.ClassWork;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public final class ImmutableClass {
    private final String str1;
    private final String str2;
    private final LocalDate mandate;
    private final ArrayList<String> colors;

    public ImmutableClass(String str1, String str2, LocalDate mandate, ArrayList<String> colors) {
        super();
        this.str1 = str1;
        this.str2 = str2;
        this.mandate = mandate;
        ArrayList<String> temp = new ArrayList<>();
        for (String color : colors) {
            temp.addLast(color);
        }
        this.colors = temp;
    }

    @Override
    public String toString() {
        return "ImmutableClass{" +
                "str1='" + str1 + '\'' +
                ", str2='" + str2 + '\'' +
                ", mandate=" + mandate +
                ", colors=" + colors +
                '}';
    }

    public String getStr1() {
        return str1;
    }

    public ArrayList<String> getColors() {
        return (ArrayList<String>) colors.clone();
    }

    public LocalDate getMandate() {
        return mandate;
    }

    public String getStr2() {
        return str2;
    }


}
