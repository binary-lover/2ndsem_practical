// frequency of each character in a string 

#include <iostream>

using namespace std;

int main() {
  string str = "Hello world!";
  int freq[256] = {0};

  for (char c : str) {
    freq[c]++;
  }

  for (int i = 0; i < 256; i++) {
    if (freq[i] > 0) {
      cout << (char)i << ": " << freq[i] << endl;
    }
  }

  return 0;
}