package Day06.ClassWorkAssignment.ToyManifactComp;

import java.util.Comparator;

public class ToyIdComparator implements Comparator<Toy> {

    @Override
    public int compare(Toy o1, Toy o2) {
        return o1.getProductId() - o2.getProductId();
    }
}
