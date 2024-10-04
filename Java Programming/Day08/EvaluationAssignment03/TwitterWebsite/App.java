package Day08.EvaluationAssignment03.TwitterWebsite;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class App {
    public static void main(String[] args) {
        List<Tweet> tweetLi = WebSite.initiateTweets();

        System.out.println("\n_________________tweets in current year___________________");
        int currentYear = 2023;
        tweetLi.stream()
                .filter((tweet) -> tweet.getDate().getYear() == currentYear)
                .forEach((tweet) -> System.out.println(
                        "ID:" + tweet.getTweetId() + " - " + tweet.getDate()
                ));

        System.out.println("\n_________________List of All Tweets for hashtag___________________");
        String hashtag = "#hash1";
        tweetLi.stream()
                .filter((tweet) -> tweet.getHashtags().contains(hashtag))
                .forEach((tweet) -> System.out.println(
                        "ID:" + tweet.getTweetId() + " - " + tweet.getHashtags()
                ));

        System.out.println("\n_________________Count tweets by subject___________________");
        tweetLi.stream()
                .collect(Collectors.groupingBy(Tweet::getSubject))
                .forEach((k, v) -> System.out.println(
                        k + " -----> " + v.size()
                ));

        System.out.println("\n_________________Tweets with more than 10k views___________________");
        tweetLi.stream()
                .filter((twet) -> (twet.getViews() > 10000))
                .forEach((twet) -> System.out.println(
                        "ID:" + twet.getTweetId() + " - " + twet.getViews()
                ));

        System.out.println("\n_________________Top 5 Trending tweets___________________");
        tweetLi.stream()
                .sorted(Comparator.comparing(Tweet::getViews).reversed())
                .limit(5)
                .forEach((twet) -> System.out.println(
                        "ID:" + twet.getTweetId() + " ------> " + twet.getViews()
                ));

    }
}
