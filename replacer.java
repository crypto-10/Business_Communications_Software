import java.util.Scanner;
import java.io.File;
import java.util.*;
import java.security.SecureRandom;
import java.util.Arrays;
import java.io.FileNotFoundException; 
public class replacer {
    public static void main(String[] args) {
try {
      File myObj = new File("keys.txt");
      String key = "";
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        key += key + data;
      }
      myReader.close();
      String[] skey = key.split(" ");
      String alp1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ=_0123456789-!@#$%^&*()`:\"'.<>?/[]{};+,\\~|";
      List<String> letters = Arrays.asList(alp1.split(""));
      SecureRandom repeat = new SecureRandom();
      for(int rep = repeat.nextInt(10); rep > 0; rep--)
      {
      Collections.shuffle(letters, new SecureRandom());
      }
      String let = String.join("", letters);
      System.out.print(let);
      for(String k : skey){
      //System.out.println(k);
      String k2 = k.substring(3,4);
      //System.out.println(k2);
      int i = alp1.indexOf(k2);
      StringBuffer k3 = new StringBuffer(k);
      //System.out.println(i);
      char ch = let.charAt(i);
      k3.setCharAt(3, ch);
      k = k3.toString();
      System.out.print(k + " ");
      }
    }
catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace(); 
    }
    }
}



