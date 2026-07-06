#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

double dist(vector<pair<int, int>> &arr, int i, int j) {
  return sqrt(pow(arr[i].first - arr[j].first, 2) +
              pow(arr[i].second - arr[j].second, 2));
}

double dfs(vector<pair<int, int>> &arr, vector<double> &dp, int mask) {
  int n = arr.size();
  if (mask == (1 << n) - 1)
    return 0.0;
  if (dp[mask] != -1)
    return dp[mask];

  double minVal = numeric_limits<double>::infinity();
  for (int i = 0; i < n; i++) {
    if (mask & (1 << i))
      continue;
    for (int j = i + 1; j < n; j++) {
      if (mask & (1 << j))
        continue;
      int newMask = mask | (1 << i) | (1 << j);
      minVal = min(minVal, dist(arr, i, j) + dfs(arr, dp, newMask));
    }
    break;
  }
  return dp[mask] = minVal;
}

int main() {
  while (true) {
    int n;
    cin >> n;
    if (n == 0)
      break;
    n *= 2;

    vector<pair<int, int>> arr;
    for (int i = 0; i < n; i++) {
      string name;
      int x, y;
      cin >> name >> x >> y;
      arr.push_back(make_pair(x, y));
    }

    vector<double> dp(1 << n, -1.0);
    dp[dp.size() - 1] = 0;
    cout << fixed << setprecision(2) << dfs(arr, dp, 0) << endl;
  }
  return 0;
}
