package Day06.ClassWork.FunctionalProgramming;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class DemoLambda1 {
    public boolean operateOnNum(Predicate p, int n){
        return p.test(n);
    }

    public List<Integer> operateOnNum(Predicate p, List<Integer> n){
        List<Integer> filtered = new ArrayList<>();
        for(Integer i : n){
            if(p.test(i)){
                filtered.add(i);
            }
        }
        return filtered;
    }

    public static void main(String[] args) {
        Integer[] nums = {12, -234, 204, 29, -50, 0, -45, 243};

        List<Integer> vals = Arrays.asList(nums);
        DemoLambda1 demo = new DemoLambda1();

        boolean ispositive = demo.operateOnNum((n) -> n > 0, -12);
        System.out.println(ispositive);

        List<Integer> positives = demo.operateOnNum((n) -> n>0, vals);
        System.out.println(positives);

        System.out.println(demo.operateOnNum((n) -> n % 100 == 0, Arrays.asList(100, 200, 300, 434, 234, 283, 540)));
    }
}
