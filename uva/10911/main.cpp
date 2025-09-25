#include <iostream>
#include <string>

using namespace std;

int main() {
  while (true) {
    int n;
    cin >> n;
    cout << n;
    if (n == 0) break;

    while (n) {
      n--;
      string str;
      cin >> str;
      cout << str;
    }
  }
}
