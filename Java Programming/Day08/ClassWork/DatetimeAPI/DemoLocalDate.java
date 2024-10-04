package Day08.ClassWork.DatetimeAPI;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalAdjuster;
import java.time.temporal.TemporalAdjusters;
import java.util.stream.Stream;

public class DemoLocalDate {
    public static <Period> void main(String[] args) {

        LocalDate today = LocalDate.now();
        System.out.println(today);

        LocalDate diwali = LocalDate.of(2025, 11, 1);
        System.out.println(diwali);


        java.time.Period timeToDiwali = today.until(diwali);
        System.out.println(timeToDiwali);
        System.out.println(timeToDiwali.getYears() + " Years " + timeToDiwali.getMonths() +
                " months " + timeToDiwali.getDays() + " day(s)");

        long daysToDiwali = today.until(diwali, ChronoUnit.DAYS);
        System.out.println(daysToDiwali + " Days");

        System.out.println(today.getDayOfMonth());
        System.out.println(today.getDayOfWeek());
        System.out.println(today.getMonthValue());
        System.out.println(today.getMonth());
        System.out.println(today.getYear());

        LocalDate tomorrow = today.plusDays(1);
        System.out.println(tomorrow);
        LocalDate nextfriday = today.plusDays(7);
        System.out.println(nextfriday);

        System.out.println("____________________________________________");
        Stream<LocalDate> currentyear = LocalDate.of(2024, 1, 1).
                datesUntil(LocalDate.of(2025, 1, 1));

        currentyear.filter((date) -> date.getDayOfWeek().equals(DayOfWeek.FRIDAY))
                .filter((date) -> date.getDayOfMonth() == 13).forEach(System.out::println);


        System.out.println(today.with(TemporalAdjusters.firstDayOfMonth()).getDayOfWeek());
        System.out.println(today.with(TemporalAdjusters.firstDayOfNextMonth()).getDayOfWeek());
        System.out.println(today.with(TemporalAdjusters.next(DayOfWeek.THURSDAY)));
        System.out.println(today.with(TemporalAdjusters.firstInMonth(DayOfWeek.SUNDAY)));
    }
}
