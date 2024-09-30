package Day06.ClassWork.MediaHierarchy;

public class Songs extends Media{

    private String title;
    private int srno;

    public Songs(String title, int srno){
        this.title = title;
        this.srno = srno;
    }

    @Override
    public void play(){
        System.out.println("Song " + title+  " is playing");
    }

    @Override
    public String toString() {
        return "Songs{" +
                "title='" + title + '\'' +
                ", srno=" + srno +
                '}';
    }

}
