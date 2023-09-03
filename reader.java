import java.util.Scanner;
import java.io.File;
import java.util.Arrays;
import java.io.FileNotFoundException; 
public class replacer {
    public static void main(String[] args) {
try {
      File myObj = new File("Dkeys.txt");
      String key = "";
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        key += key + data;
      }
      myReader.close();
      String let = key.substring(0, 94);
      //System.out.println(let);
      String[] skey = key.substring(94, key.length()).split(" ");
      String alp2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ=_0123456789-!@#$%^&*()`:\"'.<>?/[]{};+,\\~|";
      for(String k : skey){
      //System.out.println(k);
      String k2 = k.substring(3,4);
      //System.out.println(k2);
      int i = let.indexOf(k2);
      StringBuffer k3 = new StringBuffer(k);
      //System.out.println(i);
      char ch = alp2.charAt(i);
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



