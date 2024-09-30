package Day06.ClassWorkAssignment.ToyManifactComp;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class ToyStore {
    ArrayList<Toy> stock;

    public void filterByCategory(String category){
        ArrayList<Toy> filteredToys = new ArrayList<>();
        for (Toy toy : this.stock) {
            if (toy.getCategory().equals(category)) filteredToys.add(toy);
        }
        System.out.println();
        printByAttribute("category", filteredToys);

    }

    public void toysForAge(double age){
        // Forming the List
        ArrayList<Toy> toysForAge = new ArrayList<>();
        for (Toy toy : this.stock) {
            if (toy.getAge() <= age){
                toysForAge.add(toy);
            }
        }
        // Printing the List
        printByAttribute("age", toysForAge);
    }

    public void toysInPriceRange(int lowerRange, int upperRange){
        // Forming The List
        ArrayList<Toy> toysInRange = new ArrayList<>();
        for (Toy toy : this.stock) {
            if (lowerRange <= toy.getPrice() && toy.getPrice() <= upperRange){
                toysInRange.add(toy);
            }
        }
        // Printing The list
        printByAttribute("price", toysInRange);
    }
    public void printByAttribute(String attrName, ArrayList<Toy> toyList) {
        try {
            if (toyList == null) toyList = this.stock;
            Field field = Toy.class.getDeclaredField(attrName);
            field.setAccessible(true);
            for (Toy toy : toyList) {
                System.out.println(toy.getName() + " -> " + field.get(toy));
            }
        }
        catch (NoSuchFieldException | IllegalAccessException e){
            System.out.println(e.getMessage());
        }
    }

    public void findOldStocks(int yearDiff){
        ArrayList<Toy> toyList = new ArrayList<>();
        for (Toy toy : this.stock) {
            if (2024 - toy.getManifactMonthyear().year > yearDiff){
                toyList.add(toy);
            }
        }
        for (Toy toy : toyList) {
            System.out.println(toy.getName() + " ---> " + toy.getManifactMonthyear().year);
        }
    }

    public void groupByCategory(){
        HashMap<String, ArrayList<String>> toyMap = new HashMap<>();
        for (Toy toy : this.stock) {
            String currCat = toy.getCategory();
            if (toyMap.containsKey(currCat)){
                toyMap.get(currCat).add(toy.getName());
            }
            else{
                toyMap.put(currCat, new ArrayList<>());
                toyMap.get(currCat).add(toy.getName());
            }
        }
        for (Map.Entry<String, ArrayList<String>> entry: toyMap.entrySet()){
            System.out.println(entry.getKey() + " ---> " + entry.getValue());
        }

    }

    public void sortToysById(){
        this.stock.sort(new ToyIdComparator());
    }

    public void sortToysByRating(){
        this.stock.sort(new ToyRatingComparator());
    }

    public void sortToysByPrice(){
        Collections.sort(this.stock, new ToyPriceComapartor());
    }

    public ToyStore(ArrayList<Toy> stock){
        this.stock = stock;
    }



}
