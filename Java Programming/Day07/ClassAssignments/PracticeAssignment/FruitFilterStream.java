package Day07.ClassAssignments.PracticeAssignment;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class FruitFilterStream {
    public static void main(String[] args) {

        ArrayList<String> fruits = new ArrayList<>(List.of(new String[]{"Mango", "orange", "Grapes", "apple", "Banana", "Strawberry", "watermelon"}));

        Stream<String> stream = fruits.stream();

        System.out.println("\n_______________uppercase_______________");
        List<String> upperCaseStrings = stream.map(String::toUpperCase).toList();
        System.out.println(upperCaseStrings);

        System.out.println("\n_______________lowercase_______________");
        List<String> lowerCaseStrings = fruits.stream().map(String::toLowerCase).toList();
        System.out.println(lowerCaseStrings);

        System.out.println("\n_______________less than 'n' in ascending order_______________");
        List<String> lessThan_n_Ascending = fruits.stream().filter((str) -> {
            char temp = str.toLowerCase().charAt(0);
            return 0 > ((int) temp - (int) 'n');
        }).sorted(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (int) o1.toLowerCase().charAt(0) - (int) o2.toLowerCase().charAt(0);
            }
        }).toList();
        System.out.println(lessThan_n_Ascending);

//        System.out.println("_______________less than 'n' in descending order_______________");
//        List<String> lessThan_n_Descending = fruits.stream().filter((str) -> {
//            char temp = str.toLowerCase().charAt(0);
//            return 0 > ((int) temp - (int) 'n');
//        }).sorted(Comparator.reverseOrder()).toList();
//        System.out.println(lessThan_n_Ascending);

        System.out.println("\n_______________less than 'n' in descending order_______________");
        List<String> lessThan_n_Descending = fruits.stream().filter((str) -> {
            char temp = str.toLowerCase().charAt(0);
            return 0 > ((int) temp - (int) 'n');
        }).sorted(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
//                System.out.println(o1.compareTo(o2));
                return - (int) o1.toLowerCase().charAt(0) + (int) o2.toLowerCase().charAt(0);
            }
        }).toList();
        System.out.println(lessThan_n_Descending);

        System.out.println("\n_______________Fruits with uppercase names_______________");
        List<String> upperCaseNames = fruits.stream().filter((str) -> ((int) str.charAt(0) <= 90 && (int) str.charAt(0) >= 65)).toList();
        System.out.println(upperCaseNames);

//        System.out.println("\n_______________6 letters and descending_______________");
//        List<String> sixAndDescending = fruits.stream()
//                .filter((str) -> str.length() <= 6)
//                .sorted(new Comparator<String>() {
//                    @Override
//                    public int compare(String o1, String o2) {
//                        return o2.compareToIgnoreCase(o1);
//                    }
//                })
//                .toList();
//        System.out.println(sixAndDescending);

        System.out.println("\n_______________6 letters and descending_______________");
        List<String> sixAndDescending = fruits.stream()
                .filter((str) -> str.length() <= 6)
                .sorted(String::compareToIgnoreCase)
                .toList();
        System.out.println(sixAndDescending);
    }
}
