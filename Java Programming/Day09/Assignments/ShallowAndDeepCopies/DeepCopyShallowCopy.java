package Day09.Assignments.ShallowAndDeepCopies;

public class DeepCopyShallowCopy {

    int abc = 4;
    int pqr = 5;

    public DeepCopyShallowCopy(int pqr, int abc) {
        this.pqr = pqr;
        this.abc = abc;
    }

    public void setInternalObject(int a){
        temp = new Abc(a);
    }


    class Abc {
        public int num = 3;

        public Abc(int num) {
            this.num = num;
        }

        public void displayNum(){
            System.out.println(num);
        }

        @Override
        public String toString() {
            return "Abc{" +
                    "num= " + num +
                    '}';
        }
    }

    Abc temp = new Abc(1000);

    @Override
    public String toString() {
        return "abc = " + abc + " pqr =" + pqr + " Internal obj = " + temp;
    }

    public static void main(String[] args) {

        DeepCopyShallowCopy obj = new DeepCopyShallowCopy(100,200);
        DeepCopyShallowCopy other = obj;

        System.out.println("Orignal obj");
        System.out.println(obj);
        System.out.println("Shallow copy obj");
        System.out.println(other);
        System.out.println("After setting");
        other.setInternalObject(50000);
        System.out.println("Orignal obj");
        System.out.println(obj);
        System.out.println("Shallow copy obj");
        System.out.println(other);




    }

}
