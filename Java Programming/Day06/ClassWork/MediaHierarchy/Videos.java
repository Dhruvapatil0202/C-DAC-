package Day06.ClassWork.MediaHierarchy;

public class Videos extends Media{

    private int srno;
    private String title;

    public Videos(int srno, String title){
        this.srno = srno;
        this.title = title;
    }

    @Override
    public void play(){
        System.out.println("Video " + title+  " is playing");
    }

    @Override
    public String toString() {
        return "Videos{" +
                "srno=" + srno +
                ", title='" + title + '\'' +
                '}';
    }
}
