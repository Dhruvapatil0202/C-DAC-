package Day08.EvaluationAssignment03.TwitterWebsite;

import java.nio.file.attribute.FileTime;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class WebSite {

    public static List<Tweet> initiateTweets(){
        ArrayList<Tweet> tweetList = new ArrayList<>();
        tweetList.add(new Tweet(10001,"Sub1", LocalDate.of(2018, 12, 9), 10000, new TreeSet<>(Set.of("#hash4", "#hash2", "#hash3"))));
        tweetList.add(new Tweet(10002,"Sub3", LocalDate.of(2019, 9, 16), 8000, new TreeSet<>(Set.of("#hash7", "#hash2", "#hash6"))));
        tweetList.add(new Tweet(10003,"Sub2", LocalDate.of(2022, 1, 25), 4000, new TreeSet<>(Set.of("#hash9", "#hash2", "#hash6"))));
        tweetList.add(new Tweet(10004,"Sub1", LocalDate.of(2023, 5, 10), 16000, new TreeSet<>(Set.of("#hash1", "#hash7", "#hash6"))));
        tweetList.add(new Tweet(10005,"Sub2", LocalDate.of(2023, 9, 12), 20000, new TreeSet<>(Set.of("#hash9", "#hash2", "#hash5"))));
        tweetList.add(new Tweet(10006,"Sub1", LocalDate.of(2024, 7, 15), 1000, new TreeSet<>(Set.of("#hash1", "#hash8", "#hash5"))));
        tweetList.add(new Tweet(10007,"Sub3", LocalDate.of(2021, 1, 7), 11000, new TreeSet<>(Set.of("#hash3", "#hash8", "#hash5"))));
        tweetList.add(new Tweet(10008,"Sub3", LocalDate.of(2022, 8, 20), 3000, new TreeSet<>(Set.of("#hash1", "#hash8", "#hash7"))));


        return tweetList;
    }
}
