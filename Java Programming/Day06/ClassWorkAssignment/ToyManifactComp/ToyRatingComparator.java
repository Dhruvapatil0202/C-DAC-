package Day06.ClassWorkAssignment.ToyManifactComp;

import java.util.Comparator;

public class ToyRatingComparator implements Comparator<Toy> {

    @Override
    public int compare(Toy o1, Toy o2) {
        return (int) (10 * o1.getRating() - 10 * o2.getRating());
    }
}
