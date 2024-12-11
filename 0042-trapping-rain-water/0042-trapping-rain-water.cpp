#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  int trap(std::vector<int> &height) {
    int n = height.size();
    std::vector<int> left_max(n), right_max(n);

    int running_max = 0;

    for (int i = 0; i < n; i++) {
      running_max = std::max(running_max, height[i]);

      left_max[i] = running_max;
    }

    running_max = 0;
    for (int i = (n - 1); i >= 0; i--) {
      running_max = std::max(running_max, height[i]);

      right_max[i] = running_max;
    }

    int total_water = 0;

    for (int i = 0; i < n; i++) {
      int water_here = std::min(left_max[i], right_max[i]) - height[i];
      total_water += water_here;
    }
    return total_water;
  }
};

int main() {
  Solution solution;

  // Example 1
  std::vector<int> height1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
  int output1 = solution.trap(height1);
  std::cout << "Example 1: " << output1 << std::endl; // Expected output: 6

  // Example 2
  std::vector<int> height2 = {4, 2, 0, 3, 2, 5};
  int output2 = solution.trap(height2);
  std::cout << "Example 2: " << output2 << std::endl; // Expected output: 9

  return 0;
}
