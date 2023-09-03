#include <iostream>
#include <string>
#include <ctype.h>
#include <fstream>
#include<math.h>
using namespace std;
int main(){
  ifstream secfile("Ukeys.txt");
  if (secfile.is_open()){
  string data, get;
  while (getline(secfile, data)){
  get = get + data;
  }
  string line = get;
  string wrd = "";
  string word = " ";
  for(int i = 0; i < 105; i++){
  word = word + " ";
  }
  //int x = 0;
  int a;
  int count = 0;
  string L;
  double b;
  //while (x <6){
  //x++;
  for (auto z : line)
    {
        if (z == ' ')
        {
    int pos = wrd.find("|"); 
    string sub = wrd.substr(pos + 1, wrd.length());
    string sub2 = wrd.substr(0,3);
    L = wrd[3];
    int eq = L.compare("`");
    int pq = L.compare("~");
    if(eq == 0)
      L = ' ';
    else if(pq == 0)
      L = '.';
    a = stoi(sub2); //wa
    b = stod(sub); //n
  double c = (((((b - pow(a,7))* 36882.81)*(89.729*a)) /(41.12+(a*1.632)) - 1529.1271) / pow(a, 8)) - a;
  c = round(c);
  word.replace(c, 1, L);
  count ++;
  //cout << word + "\n";
  wrd = "";
  }
        else {
            wrd = wrd + z;
        }
        }
  string width = "";
  word = word.substr(0, count);
  for(int i = 0; i < count + 4; i++)
    width = width + "-";
  cout << width;
  cout << "\n| " << word << " |\n"; //EDIT THIS LINE TO OUTPUT "MESSAGE RECEIVED"
  cout << width;
        //}
    }
}
