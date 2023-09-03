#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include<math.h>
using namespace std;
int main(){
  ifstream file("output.txt"); //Open files + read + initialize variables START
  ifstream indf("ind.txt");
  ifstream indk("text.txt");
  ifstream target("enter.txt"); //TARGET TO ENCRYPT
  if (file.is_open()){
    if(indf.is_open()){
      if(indk.is_open()){
        if (target.is_open()){
      string inf, ta, sa, KEY, text, in, ink, get, dat, val, k, e, bac, star, store;
      vector<string> v;
      srand(time(0));
      int w = 5;                                            // maximum index of KEY ID #2
      int ter = 0;
      int n = 0;
      int i = 0;
      int a = -1;
      int co = 0;
      int u = 0;
      srand(time(0));
      rename("enter.txt", "ENCRYPTED.txt");
      while(getline(file, inf)){                            //READ FILES - START
        KEY = KEY + inf;
  }
      while(getline(indf, dat)){
        in = in + dat;
  }
      while(getline(indk, get)){
        text = text + get;
  }
      while(getline(target, ta)){
        sa = sa + ta;
        }                                                   //READ FILES - END
      for(int i = 0; i < sa.length(); i++)
      {
      if(sa[i] == ' ')
      sa[i] = '`';
      else if(sa[i] == '.')
      sa[i] = '~';
      }
      text = sa;
      while (i < text.size()){
        while(in[ter] != ' '){
          star = star + in[ter];
          ter++;
      }                                                 //END INITIALIZATION AND READING
          int pop = stoi(star);                         //convert the initialized string numbers into integers and prepare encryption
          k = text[i] + star;
          e = e + k + '.';
          store = KEY[pop];
          text.replace(n, 1, store);
          val = val + star;
          ter ++;
          bac = ink[ter];
          star = in[ter];
          ter ++;
          n ++;
          i ++;                                        //END
      }
        string key1;                                   //START RANDOMIZING SCRIPT FOR KEY#1 
        vector<int> num;
        for (int sef = 0; sef < e.size(); sef++){
            key1  = "";
        for(int zer = 0; zer < w; zer++){
            if(e[sef] != '.'){
            key1 = key1 + e[sef];
            sef++;
            }
          }
          v.push_back(key1);
        }
        string out;
        int gu = 0;
        while(gu < v.size()){                   //THIS OUTPUTS KEY ID#1
            int n = rand() % v.size();
            int wa = (rand() % 900) + 100;
            if (find(num.begin(), num.end(), n) != num.end()){
            num.push_back(n);}
            else{num.push_back(n);
              double fac = ((((((n + wa) * pow(wa,8)) - 1529.1271)) * (41.12+(wa*1.632)) / (89.729 * wa)) / 36882.81) + pow(wa,7);
              cout << to_string(wa) + v[n] + "|";
              cout << to_string(fac) + " ";
             gu++;
            }
        }                                                   //END OF RANDOMIZER SCRIPT
    //cout << "\n" << "------------------------------";
    //cout << "\n" << "[-]KEY ID#2: " << "\n";              //OUTPUTS KEY ID#2
    //cout << KEY << "\n" "\n";
    //cout << "[!] SUCCESSFULLY ENCRYPTED" << '\n';
    ofstream target("ENCRYPTED.txt");
    ofstream ("enter.txt");
    if (target.is_open()){
    target << text << endl;
    }
    }
  }
  }
  }
  indk.close();                                         //CLOSE FILES
  indf.close();
  file.close();
  target.close();
  return 0;
  }

