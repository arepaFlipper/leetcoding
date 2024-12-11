#include <vector>
class Solution {
private:
  int most_common_m(std::vector<std::vector<int>> &m_s) {
    int len = m_s.size();
    std::vector<int> counter;
    int most;
    for (int i; i < len; ++i) {
      for (int j = i + 1; j < len; ++j) {
        counter[i + j] = m_s[i][j];
        most = m_s[i][j];
      }
    }
  }

public:
  int maxPoints(std::vector<std::vector<int>> &points) {
    int len = points.size();
    if (len <= 2) {
      return len;
    }
    std::vector<std::vector<int>> m;
    for (int i = 0; i < len; ++i) {
      int xi = points[i][0];
      int yi = points[i][1];
      for (int j = i + 1; j < len; ++i) {
        int xj = points[j][0];
        int yj = points[j][1];
        int delta_x = xi - xj;
        int delta_y = yi - yj;
        /* int cur_m >> m[j]; */
        if (delta_y == 0 || delta_y == 0) {
          m[i][j] = 0;
        }
        m[i][j] = delta_y / delta_x;
      }
    }
  }
};
