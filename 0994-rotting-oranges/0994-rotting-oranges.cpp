#include <queue>
#include <vector>

class Solution {

private:
  int drow[4] = {0, 0, -1, 1};
  int dcol[4] = {1, -1, 0, 0};

public:
  int orangesRotting(std::vector<std::vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();

    auto dist = std::vector<std::vector<int>>(m, std::vector<int>(n, -1));

    std::queue<std::pair<int, int>> q;

    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        if (grid[r][c] == 2) {
          dist[r][c] = 0;
          q.push({r, c});
        }
      }
    }

    while (!q.empty()) {
      std::pair<int, int> cur = q.front();
      q.pop();
      for (int d = 0; d < 4; ++d) {
        int new_row = cur.first + drow[d];
        int new_col = cur.second + dcol[d];
        if (0 <= new_row && new_row < m && 0 <= new_col && new_col < n) {
          // a fresh orange
          if (grid[new_row][new_col] == 1) {
            if (dist[new_row][new_col] == -1) {
              dist[new_row][new_col] = dist[cur.first][cur.second] + 1;
              q.push({new_row, new_col});
            }
          }
        }
      }
    }

    int answer = 0;

    for (int row = 0; row < m; ++row) {
      for (int col = 0; col < n; ++col) {
        if (grid[row][col] == 1 && dist[row][col] == -1) {
          return -1;
        } else if (grid[row][col] == 1) {
          answer = std::max(answer, dist[row][col]);
        }
      }
    }
    return answer;
  }
};
