package Day05.PracticeAndClassWork.collectionIntro;

public class DemoGeneric<T> {
    T data;

    public DemoGeneric(T data){
        this.data = data;
    }

    public String getClassName(){
        return data.getClass().toString();
    }

    public static void main(String[] args) {
        DemoGeneric<Integer> iobj = new DemoGeneric<Integer>(2004);
        DemoGeneric<String> sobj = new DemoGeneric<>("Hello");

        System.out.println(iobj.getClassName());
        System.out.println(sobj.getClassName());
    }
}
