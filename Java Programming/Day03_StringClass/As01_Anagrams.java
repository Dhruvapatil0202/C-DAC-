package Day03_StringClass;
import java.util.HashMap;
import java.util.Objects;

public class As01_Anagrams {
    public static boolean checkAnagrams(String str1, String str2){

        HashMap<Character, Integer> cc1 = new HashMap<Character, Integer>();
        for(int i = 0; i < str1.length(); i++){
            char potKey = str1.charAt(i);
            int val = cc1.getOrDefault(potKey, 0) + 1;
            cc1.put(potKey, val);
        }

        HashMap<Character, Integer> cc2 = new HashMap<Character, Integer>();
        for(int i = 0; i < str2.length(); i++){
            char potKey = str2.charAt(i);
            int val = cc2.getOrDefault(potKey, 0) + 1;
            cc2.put(potKey, val);
        }

        for(char key: cc1.keySet()){
            if (!cc2.containsKey(key) || !Objects.equals(cc2.get(key), cc1.get(key))){
                return false;
            }
        }

        for(char key: cc2.keySet()){
            if (!cc1.containsKey(key) || !Objects.equals(cc1.get(key), cc2.get(key))){
                return false;
            }
        }

        return true;

    }

    public static void main(String[] args) {
        String str1 = "CheckAnagrams ";
        String str2 = "Check Anagrams";
        String str3 = "Check Anagrams";

        boolean out = checkAnagrams(str1, str2);
        if (out) System.out.println("Strings are Anagrams");
        else System.out.println("Strings are Not Anagrams");





//
    }
}
