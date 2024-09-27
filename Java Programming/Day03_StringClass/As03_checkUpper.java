package Day03_StringClass;

public class As03_checkUpper {
    public static boolean checkUpper(String str){
        for(int i = 0; i < str.length(); i++){
            int asci = (int) str.charAt(i);
            if (asci > 90 || asci < 65){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        String str1 = "JoHHONVONEOleo";
        System.out.println(checkUpper(str1));
    }
}
