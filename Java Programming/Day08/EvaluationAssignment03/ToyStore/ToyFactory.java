package Day08.EvaluationAssignment03.ToyStore;

import java.util.ArrayList;



public class ToyFactory {

    private ArrayList<Toy> stock = new ArrayList<>();

    public ArrayList<Toy> manufactureToys(){


        Toy toy1 = new Toy(1234, "RC Car", 2500.00, "Battery Operated", 8, new ToyDate("Feb", 2017), new ToyDate("May", 2017));
        Toy toy2 = new Toy(1235, "Lego Set", 3500.50, "Building Blocks", 6, new ToyDate("Jan", 2018), new ToyDate("April", 2018));
        Toy toy3 = new Toy(1236, "Action Figure", 1500.75, "Action Figures", 5, new ToyDate("Dec", 2015), new ToyDate("March", 2016));
        Toy toy4 = new Toy(1237, "Doll House", 4500.99, "Pretend Play", 4, new ToyDate("Sept", 2017), new ToyDate("Dec", 2017));
        Toy toy5 = new Toy(1237, "Kitchen House", 5500.99, "Pretend Play", 4, new ToyDate("Feb", 2023), new ToyDate("Dec", 2023));
        Toy toy6 = new Toy(1238, "Puzzle Set", 1200.00, "Puzzles", 7, new ToyDate("March", 2017), new ToyDate("June", 2017));
        Toy toy7 = new Toy(1239, "Train Set", 5000.00, "Battery Operated", 9, new ToyDate("July", 2019), new ToyDate("Aug", 2019));
        Toy toy8 = new Toy(1240, "Teddy Bear", 800.50, "Soft Toys", 3, new ToyDate("April", 2024), new ToyDate("Oct", 2024));
        Toy toy9 = new Toy(1241, "Board Game", 1800.20, "Games", 10, new ToyDate("Aug", 2015), new ToyDate("Nov", 2015));
        Toy toy10 = new Toy(1242, "Remote Helicopter", 6000.75, "Battery Operated", 12, new ToyDate("April", 2020), new ToyDate("May", 2020));

        stock.add(toy1);
        stock.add(toy2);
        stock.add(toy3);
        stock.add(toy4);
        stock.add(toy5);
        stock.add(toy6);
        stock.add(toy7);
        stock.add(toy8);
        stock.add(toy9);
        stock.add(toy10);

        return stock;

    }



}


