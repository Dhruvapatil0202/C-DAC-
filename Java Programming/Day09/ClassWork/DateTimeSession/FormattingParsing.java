package Day09.ClassWork.DateTimeSession;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class FormattingParsing {
    public static void main(String[] args) {
        // Default format
        LocalDateTime dt = LocalDateTime.of(2024, 11, 12, 16, 23, 40);
        System.out.println(dt);

        // Custom format
        String date = dt.format(DateTimeFormatter.ofPattern("dd/MM/yy hh:mm:ss"));
        System.out.println(date);

        String date2 = dt.format(DateTimeFormatter.ofPattern("dd-MMM-yyyy HH:mm:ss"));
        System.out.println(date2);

        String mydate = "2024/12/12 04:23:40";

        LocalDateTime mydt = LocalDateTime.parse(mydate,
                DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss"));
        System.out.println(mydt);
    }
}
