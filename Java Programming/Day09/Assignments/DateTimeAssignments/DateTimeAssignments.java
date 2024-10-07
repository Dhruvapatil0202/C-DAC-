package Day09.Assignments.DateTimeAssignments;

import java.time.*;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class DateTimeAssignments {
    public static void main(String[] args) {
        // Calculate your age in no of days
        System.out.println("____________________________days from birthday__________________________________");
        LocalDate birthDay = LocalDate.of(2001, 2, 3);
        LocalDate currentDay = LocalDate.now();
        System.out.println(ChronoUnit.DAYS.between(birthDay, currentDay));

        // Compute programmers day without using plusDays
        System.out.println("________________________Programmers day___________________________________");
        int year = 2025;
        LocalDate fDatofYear = LocalDate.of(year-1, 12, 31);
        LocalDate progDay = fDatofYear.plus(256, ChronoUnit.DAYS);

        System.out.println(progDay);


        // Find out all the months that started on Sundays in year 2024
        System.out.println("________________________Months Starting With Sundays___________________________________");
        int year3 = 2024;
        for (int month = 1; month < 13; month++) {
            LocalDate temp = LocalDate.of(year3, month, 1);
            if (temp.getDayOfWeek().toString().equals("SUNDAY")){
                System.out.println(temp.getMonth());
            };
        }

        // Find out all the months that started on Sundays in year 2024
        System.out.println("________________________Months Starting With Sundays___________________________________");
        Stream<LocalDate> currentYear = LocalDate.of(2024,1,1).datesUntil(LocalDate.of(2025,1,1));
        List<LocalDate> filtered = currentYear
                .filter((date) -> date.getDayOfMonth()==1)
                .filter((date) -> date.getDayOfWeek().equals(DayOfWeek.SUNDAY))
                .collect((Collectors.toList()));
        System.out.println(filtered);

        // If we leave Mumbai at 02:04 am and arrive in New York at 4:40pm how long is the flight?
        System.out.println("________________________Journey duration from Mumbai to New York___________________________________");
        ZonedDateTime indianTime = ZonedDateTime.of(LocalDateTime.of(2024,2,1,02,05), ZoneId.of("Asia/Calcutta"));
        ZonedDateTime newYorkTime = ZonedDateTime.of(LocalDateTime.of(2024,2,1,16,40), ZoneId.of("America/New_York"));

        Duration journeyDuration = Duration.between(indianTime,newYorkTime);
        System.out.println(journeyDuration);

    }
}
