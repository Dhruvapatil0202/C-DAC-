package Day06.ClassWorkAssignment.ToyManifactComp;

import java.lang.reflect.Array;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {

        // Creating the toys in and adding them in list
        ArrayList<Toy> toyList = new ArrayList<Toy>();

        toyList.add(new Toy(100, 4.2,"RC Car", 2000, 10, "Battery Operated", new DateForToyClass("Jan", 2010), new DateForToyClass("Jun", 2010)));
        toyList.add(new Toy(221, 4.5,"Wooly Elephant", 500, 7, "Soft toy", new DateForToyClass("Nov", 2020), new DateForToyClass("May", 2021)));
        toyList.add(new Toy(147, 3.9,"Battery OP- Toy Gun", 1500, 13, "Battery Operated", new DateForToyClass("Mar", 2007), new DateForToyClass("May", 2007)));
        toyList.add(new Toy(203, 4.0,"Rubber Duck", 400, 9, "Rubber Toy", new DateForToyClass("Feb", 2010), new DateForToyClass("Mar", 2010)));
        toyList.add(new Toy(250, 4.6,"Puppeted Storybook", 600, 5, "Educational", new DateForToyClass("Sept", 2015), new DateForToyClass("Jan", 2017)));
        toyList.add(new Toy(47, 3.7,"Slinky", 200, 10, "Rubber Toy", new DateForToyClass("Dec", 2017), new DateForToyClass("Jan", 2018)));
        toyList.add(new Toy(91, 4.1,"Teddy Bear", 300, 5, "Soft toy", new DateForToyClass("Apr", 2018), new DateForToyClass("Oct", 2018)));
        toyList.add(new Toy(381, 4.8,"Alphabet block set", 500, 6, "Educational", new DateForToyClass("Jan", 2021), new DateForToyClass("Jun", 2021)));

        ToyStore shop = new ToyStore(toyList);

        shop.filterByCategory("Soft toy");

        int ind = Collections.binarySearch(toyList, new Toy(203, 0,null, 0, 0, null, null, null), new ToyIdComparator());
        System.out.println("\n" + shop.stock.get(ind));

        System.out.println("\n-----------------Finding Range---------------------");
        shop.toysInPriceRange(300, 1000);

        System.out.println("\n-----------------Findnig Toys for Specific Age---------------");
        shop.toysForAge(10);

        System.out.println("\n----------------Sorting toys based on ToyId-------------------");
        shop.sortToysById();
        shop.printByAttribute("productId", null);

        System.out.println("\n----------------Sorting toys based on ToyRating-------------------");
        shop.sortToysByRating();
        shop.printByAttribute("rating", null);

        System.out.println("\n----------------Sorting toys based on ToyPrice-------------------");
        shop.sortToysByPrice();
        shop.printByAttribute("price", null);

        System.out.println("\n-----------------List of Old Stock-----------------------");
        shop.findOldStocks(5);

        System.out.println("\n-----------------Category wise seperation-----------------------");
        shop.groupByCategory();



    }
}
