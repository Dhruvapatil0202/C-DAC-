package Day05.PracticeAndClassWork;


public class StringMethods {
    public static String convertToLower(String s) throws EmptyStringException {
        if(s.isEmpty()){
            throw new EmptyStringException("Error: String is empty ");
        }
        else return s.toLowerCase();
    }

    public static void main(String[] args) {
        String s = "Spark";
        String s1 = "";
        try{
            String lower = convertToLower(s1);
            System.out.println(lower);
        }
        catch(EmptyStringException e){
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}


