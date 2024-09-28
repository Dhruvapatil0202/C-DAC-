package Day05.PracticeAndClassWork.collectionIntro;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class DemoMap {
    public static void main(String[] args) {

        Map<String, Integer> map = new HashMap<>();
        map.put("one", 100);
        map.put("two", 200);
        map.put("three", 300);

        System.out.println(map.get("two"));

        Set<String> keyset = map.keySet();
        for (String key : keyset) {
            System.out.println(key + " ----> " + map.get(key));
        }

        System.out.println(map.remove("two"));

        System.out.println("_____________________________");

        for(Map.Entry<String, Integer> entry: map.entrySet()){
            System.out.println(entry.getKey() + " -------------> " + entry.getValue());
            System.out.println(entry.toString());

        }

    }
}
