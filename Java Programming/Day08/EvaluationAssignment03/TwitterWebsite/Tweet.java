package Day08.EvaluationAssignment03.TwitterWebsite;

import java.time.LocalDate;
import java.util.TreeSet;

public class Tweet {
    private int tweetId;
    private String subject;
    private LocalDate date;
    private int views;
    private TreeSet<String> hashtags;

    public Tweet(int tweetId, String subject, LocalDate date, int views,  TreeSet<String> hashtags) {
        this.tweetId = tweetId;
        this.subject = subject;
        this.hashtags = hashtags;
        this.views = views;
        this.date = date;
    }

    @Override
    public String toString() {
        return "Tweet{" +
                "subject='" + subject + '\'' +
                ", date=" + date +
                ", views=" + views +
                ", hashtags=" + hashtags +
                '}';
    }
    public int getTweetId(){
        return tweetId;
    }

    public void setTweetId(int newId){
        this.tweetId = newId;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public TreeSet<String> getHashtags() {
        return hashtags;
    }

    public void setHashtags(TreeSet<String> hashtags) {
        this.hashtags = hashtags;
    }

    public int getViews() {
        return views;
    }

    public void setViews(int views) {
        this.views = views;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
}
