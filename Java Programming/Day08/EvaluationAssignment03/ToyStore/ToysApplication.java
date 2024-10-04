package Day08.EvaluationAssignment03.ToyStore;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ToysApplication {


    public static void main(String[] args) {

        ToyFactory toyLand = new ToyFactory();
        ArrayList<Toy> stock = toyLand.manufactureToys();
        Stream<Toy> stream = stock.stream();

        Scanner sc = new Scanner(System.in);

        // Printing out the entire stock
        System.out.println("________________Printing out Stock________________");
        stock.forEach((toy) -> System.out.println("Name: " + toy.getName() + "  Id: " + toy.getProductId()));

        // Fileter the toys by category
        System.out.println("\n---------------------Filter Toys By Category---------------------");
        System.out.println("Enter the category by which you want to filter the toys:");
//        String category = sc.nextLine();
        String category = "Pretend Play";
        List<Toy> filteredStock = stream.filter(toy -> toy.getCategory().equalsIgnoreCase(category)).toList();
        filteredStock.forEach(System.out::println);
//        System.out.println(filteredStock);

        System.out.println("\n________________Filter by Price range________________");
        stock.parallelStream()
                .filter((toy) -> (toy.getPrice() > 500 && toy.getPrice() < 2000))
                .forEach((toy) -> System.out.println("Id: " + toy.getProductId() + " Name: " + toy.getName() + " Price: " + toy.getPrice()));

        System.out.println("\n________________Layered Sorting________________");
        stock.stream()
                .sorted(Comparator.comparing(Toy::getCategory).
                        thenComparing(Toy::getPrice))
                .forEach((toy) -> System.out.println("Name: " + toy.getName() + " |Category: " + toy.getCategory() + " |Price: " + toy.getPrice()));

        System.out.println("\n________________List of Old Stocks(mfg before 2019)________________");
        stock.stream()
                .filter((toy) -> toy.getMfgDate().year < 2019)
                .forEach((toy) -> System.out.println("Name: " + toy.getName() + " Mfg Year: " + toy.getMfgDate().year));

        System.out.println("\n________________Grouping by the Category________________");
        stock.stream()
                .collect(Collectors.groupingBy(Toy::getCategory))
                .forEach((k, v) -> System.out.println(k + " Count: " + v.size()));

        System.out.println("\n________________Finding Minimum and Maximum________________");
        stock.stream()
                .collect(Collectors.groupingBy(Toy::getCategory))
                .forEach((k, v) -> {
                    Optional<Toy> toy1 = v.stream().min(Comparator.comparing(Toy::getPrice));
                    Optional<Toy> toy2 = v.stream().max(Comparator.comparing(Toy::getPrice));
                    System.out.println("Category: " + k +
                            "\t|\tMinimum: " + (toy1.isPresent() ? toy1.get().getPrice() : "N/A") +
                            "\t|\tMaximum: " + (toy2.isPresent() ? toy2.get().getPrice() : "N/A" ));
                });

        System.out.println("\n________________No of Toys in Age group________________");
        stock.stream()
                .collect(Collectors.groupingBy((toy) -> {
                    double ageLim = toy.getAgeLimit();
                    if (ageLim <= 4) return "0-4";
                    else if (5 <= ageLim && ageLim <= 8 ) return "5-8";
                    else if (9 <= ageLim && ageLim <= 12) return "9-12";
                    else if (13 <= ageLim && ageLim <= 15) return "13-15";
                    else return "15+";
                })).forEach((k, v) -> System.out.println( k + " ----> " + v.size()));



    }

}

