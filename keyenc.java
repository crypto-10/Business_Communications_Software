import java.util.Scanner;
import java.io.File;
import java.util.Arrays;
import java.io.FileNotFoundException; 
public class replacer {
    public static void main(String[] args) {
try {
File myObj = new File("Fkeys.txt");
      String wkey = "";
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        wkey += wkey + data;
      }
      String qkey = wkey.substring(0,94);
      String lkey = wkey.substring(94,wkey.length());
      myReader.close();
      String[] skey = qkey.split("");
      String alp1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXWYZ=_0123456789!@#$%^&*()`:\"'.<>?/[]{};+-,\\~|";
      String alp2 = "!&|c`Q'IBs\"u?x$/MnzAh0R~rO<7w]NLapZ=W;V25Fo4*3j-968[,{v1DPg+bJqf^TXYHlikS)}KCdUm\\e%@.#(>E_ytG:";
      for(String k : skey){
      //System.out.println(k);
      //System.out.println(k2);
      int i = alp1.indexOf(k); 
      StringBuffer k3 = new StringBuffer(k);
      //System.out.println(i);
      char ch = alp2.charAt(i);
      k3.setCharAt(0, ch);
      k = k3.toString();
      System.out.print(k);
      }
      System.out.print(lkey);
    }
catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace(); 
    }
    }
}



