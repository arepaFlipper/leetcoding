#include <algorithm>
#include <iostream>
#include <ostream>
#include <vector>
class Solution {
public:
  int firstMissingPositive(std::vector<int> &nums) {
    int n = nums.size();
    std::sort(nums.begin(),nums.end());
    for (int i = 0; i < n; i++) {
      int cur = nums[i];
      while ((1<=cur)&&(cur<=n)&&(cur-1 !=i)&&(cur!=nums[cur-1])) {
        std::swap(cur, nums[cur - 1]);
      }
    }
    for (int i = 0; i < n; ++i) {
      int current = nums[i];
      if ((1>current) || (current > n) || (current - 1 != i)) {
        return i + 1;
      }
    }
    return n + 1;
  }
};
int main() {
    Solution solution;

    // Example 1
    std::vector<int> nums1 = {1, 2, 0};
    int output1 = solution.firstMissingPositive(nums1);
    std::cout << "Example 1: " << output1 << std::endl; // Expected output: 3

    // Example 2
    std::vector<int> nums2 = {3, 4, -1, 1};
    int output2 = solution.firstMissingPositive(nums2);
    std::cout << "Example 2: " << output2 << std::endl; // Expected output: 2

    // Example 3
    std::vector<int> nums3 = {7, 8, 9, 11, 12};
    int output3 = solution.firstMissingPositive(nums3);
    std::cout << "Example 3: " << output3 << std::endl; // Expected output: 1

    // Additional Example 4
    std::vector<int> nums4 = {2, 1};
    int output4 = solution.firstMissingPositive(nums4);
    std::cout << "Additional Example 4: " << output4 << std::endl; // Expected output: 3

    // Additional Example 5
    std::vector<int> nums5 = {1, 2, 0};
    int output5 = solution.firstMissingPositive(nums5);
    std::cout << "Additional Example 5: " << output5 << std::endl; // Expected output: 3

    // Additional Example 6
    std::vector<int> nums6 = {1, 1};
    int output6 = solution.firstMissingPositive(nums6);
    std::cout << "Additional Example 6: " << output6 << std::endl; // Expected output: 2

    // Additional Example 7
    std::vector<int> nums7 = {3, 4, -1, 1};
    int output7 = solution.firstMissingPositive(nums7);
    std::cout << "Additional Example 7: " << output7 << std::endl; // Expected output: 2

    return 0;
}
