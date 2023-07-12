#include <algorithm>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

class Solution {
private:
  const int dr[4] = {0, 0, -1, 1};
  const int dc[4] = {-1, 1, 0, 0};
  bool valid(int r, int c, int m, int n) {
    return (0 <= r) && (r < m) && (0 <= c) && (c < n);
  }

public:
  int cutOffTree(std::vector<std::vector<int>> &forest) {
    int m = forest.size();
    int n = forest[0].size();
    std::vector<std::pair<int, int>> locations(
        1, {0, 0}); // locations we need to visit, in order

    std::vector<std::pair<int, std::pair<int, int>>>
        priority; //(tree num, location)

    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        if (forest[row][col] > 1) {
          priority.push_back({forest[row][col], {row, col}});
        }
      }
    }
    std::sort(priority.begin(), priority.end());

    for (std::pair<int, std::pair<int, int>> tree : priority) {
      locations.push_back(tree.second);
    }

    int tot_dist = 0;

    for (int loc = 0; loc + 1 < locations.size(); loc++) {
      // go from locations[loc] to locations[loc+1]
      std::vector<std::vector<int>> dists(m, std::vector<int>(n, -1));

      std::pair<int, int> from = locations[loc];
      std::pair<int, int> to = locations[loc + 1];

      dists[from.first][from.second] = 0;

      std::queue<std::pair<int, int>> q;
      q.push(from);

      while (!q.empty()) {
        std::pair<int, int> cur = q.front();
        q.pop();
        for (int d = 0; d < 4; d++) {
          int new_r = cur.first + dr[d];
          int new_c = cur.second + dc[d];
          if (valid(new_r, new_c, m, n) && forest[new_r][new_c] != 0 &&
              (dists[new_r][new_c] == -1)) {
            dists[new_r][new_c] = dists[cur.first][cur.second] + 1;
            q.push({new_r, new_c});
          }
        }
      }
      if (dists[to.first][to.second] == -1) {
        return -1;
      } else {
        tot_dist += dists[to.first][to.second];
      }
    }
    return tot_dist;
  }
};
