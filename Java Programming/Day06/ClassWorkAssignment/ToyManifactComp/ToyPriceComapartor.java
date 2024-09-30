package Day06.ClassWorkAssignment.ToyManifactComp;

import java.util.Comparator;

public class ToyPriceComapartor implements Comparator<Toy> {
    @Override
    public int compare(Toy o1, Toy o2) {
        return (int) Math.floor(o1.getPrice() - o2.getPrice());
    }
}
