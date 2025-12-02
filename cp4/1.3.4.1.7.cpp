#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

void dfs(string &chars, vector<string> &res, vector<bool> &used,
         vector<char> &path) {
  if (path.size() == chars.size())
    res.push_back(string(path.begin(), path.end()));
  for (size_t i = 0; i < chars.size(); i++) {
    if (used[i])
      continue;
    used[i] = true;
    path.push_back(chars[i]);
    dfs(chars, res, used, path);
    used[i] = false;
    path.pop_back();
  }
}

int main() {
  string chars = "abcdefghyj";
  vector<string> res;
  vector<bool> used(chars.size(), false);
  vector<char> path;

  dfs(chars, res, used, path);
  printf("%zu\n", res.size());
}
