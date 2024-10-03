package Day07.Classwork;

import Day01.MathsTemp;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class DemoIntegerStream {
    public static void main(String[] args) {
        Integer[] nums = {12, 4, 7, 243, 69, 55};

        List<Integer> lst = Arrays.asList(nums);

        System.out.println("________________000________________");
        Stream<Integer> stream = lst.parallelStream();
        stream.map((n) -> Math.sqrt(n)).forEach(System.out :: println);

        System.out.println("________________001________________");
        stream = lst.parallelStream();
        List<Integer> primes = stream.filter(MathsTemp::isPrime).toList();

        System.out.println("________________002________________");
        stream = lst.stream();
        stream.distinct().sorted(Integer::compareTo).forEach(System.out::println);

        System.out.println("________________003________________");
        stream = lst.stream();
        Optional<Integer> total = stream.reduce((n1, n2) -> n1 + n2);
        if(total.isPresent()) System.out.println(total.get());

        System.out.println("________________004________________");
        stream = lst.parallelStream();
        long sum = stream.reduce(1, (n1, n2) -> n1 + n2);
        System.out.println(sum);

        System.out.println("________________005________________");
        stream = lst.stream();
        Optional<Integer> min = stream.min(Integer :: compareTo);
        if(min.isPresent()) System.out.println(min.get());

        System.out.println("________________006________________");
        stream = lst.stream();
        OptionalDouble ave = stream.mapToDouble(Double::valueOf).average();
        if(ave.isPresent()) System.out.println(ave.getAsDouble());

        stream = lst.stream();
        Optional<Integer> anyOdd = stream.filter((num) -> num > 50)
                .findAny();

        stream = lst.stream();
        List<Integer> li = stream.filter((n) -> n > 50)
                .toList();

        stream = lst.stream();
        boolean l2 = stream.allMatch((n) -> n%2==0);
        System.out.println(l2);

        boolean l3 = lst.stream().anyMatch((n)-> n%2==0);
        System.out.println(l3);

    }
}
