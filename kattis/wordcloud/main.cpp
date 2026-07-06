#include <bits/stdc++.h>

using namespace std;

int main() {
  int W, N;
  int testCase = 0;
  while (scanf("%d %d", &W, &N), W == 0 && N == 0) {
    vector<pair<int, int>> words(N);
    int maxSize = 0;
    for (size_t i = 0; i < N; i++) {
      string word;
      int amount;
      scanf("%s %d", &word, &amount);
      words.push_back(make_pair(word.size(), amount));
      maxSize = max(maxSize, (int)word.size());
    }
    int x = 0, y = 0;
    for (size_t i = 0; i < words.size(); i++) {
      int P = 8 + ceil(40.0 * (words[i].second - 4.0) / (maxSize - 4.0));
      int width = ceil(9.0 / 16.0 * words[i].first * P);
      if (x + width > W) {
        x = 0;
        y += P;
      }
      x += width + 10;
    }
    printf("COUL %d: %d", ++testCase, y);
  }
}
