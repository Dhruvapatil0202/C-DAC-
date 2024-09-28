package Day05.PracticeAndClassWork;

import java.io.File;
import java.io.IOException;

public class DemoThrow {

    public static void checkFile(String path) throws IOException{
        File f = new File(path);
        if(!f.exists()){
            throw new IOException("File not found");
        }
    }

    public static void main(String[] args) {
        try {
            File f = new File("data.txt");
            if(!f.exists()){
                throw new IOException("File not Found");
            }

        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
    }
}
