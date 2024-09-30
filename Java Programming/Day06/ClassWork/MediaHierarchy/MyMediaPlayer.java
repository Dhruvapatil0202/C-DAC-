package Day06.ClassWork.MediaHierarchy;

import java.util.ArrayList;
import java.util.List;

public class MyMediaPlayer {

    public void playMyList(List<? extends Media> medialist){
        for(Media m : medialist){
            m.play();
        }
    }

    public static void main(String[] args) {
        MyMediaPlayer player = new MyMediaPlayer();
        List<Songs> songs = new ArrayList<>();

        songs.add(new Songs( "sffwfw", 342));
        songs.add(new Songs( "vertfw", 343));
        songs.add(new Songs( "evefw", 344));
        songs.add(new Songs( "ntyrwfw", 345));

        player.playMyList(songs);
    }
}
