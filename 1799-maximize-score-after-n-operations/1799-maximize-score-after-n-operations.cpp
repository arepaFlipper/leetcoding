#include <algorithm>
#include <iostream>
#include <numeric>
#include <ostream>
#include <vector>
class Solution {
private:
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

public:
  int maxScore(std::vector<int> &nums) {
    // represents 2*(n from statement); number of bits in mask
    int n = nums.size();
    int INF = 1e9;

    std::vector<int> dp((1 << n), -INF);

    dp[(1 << n) - 1] = 0;
    for (int mask = (1 << n) - 1; mask >= 0; --mask) {
      int num_bits_set = __builtin_popcount(mask);

      if (num_bits_set % 2 == 0) {
        // even # bits set.

        int num_bits_unset = (n- num_bits_set);
        int turn = (num_bits_unset) / 2 + 1;
        for (int i = 0; i < n; i++) {
          if ((mask >> i) & 1) {
            // i-th bit is set in mask

            for (int j = i + 1; j < n; j++) {
              if ((mask >> j) & 1) {
                // j-th bit is set

                int g = gcd(nums[i], nums[j]);

                int new_mask = mask;
                new_mask ^= (1<<i); // un-set i-th bit
                new_mask ^= (1<<j); // un-set i-th bit
                
                dp[new_mask] = std::max(dp[new_mask], dp[mask] +turn * g);
              }
            }
          }
        }
      }
    }
    return dp[0];
  }
};

int main() {
    Solution solution;

    // Example 1
    std::vector<int> nums1 = {1, 2};
    int output1 = solution.maxScore(nums1);
    std::cout << "Example 1: " << output1 << std::endl; // Expected output: 1

    // Example 2
    std::vector<int> nums2 = {3, 4, 6, 8};
    int output2 = solution.maxScore(nums2);
    std::cout << "Example 2: " << output2 << std::endl; // Expected output: 11

    // Example 3
    std::vector<int> nums3 = {1, 2, 3, 4, 5, 6};
    int output3 = solution.maxScore(nums3);
    std::cout << "Example 3: " << output3 << std::endl; // Expected output: 14

    // Additional Example 4
    std::vector<int> nums4 = {1, 2};
    int output4 = solution.maxScore(nums4);
    std::cout << "Additional Example 4: " << output4 << std::endl; // Expected output: 1

    // Additional Example 5
    std::vector<int> nums5 = {3, 4, 6, 8};
    int output5 = solution.maxScore(nums5);
    std::cout << "Additional Example 5: " << output5 << std::endl; // Expected output: 11

    // Additional Example 6
    std::vector<int> nums6 = {1, 2, 3, 4, 5, 6};
    int output6 = solution.maxScore(nums6);
    std::cout << "Additional Example 6: " << output6 << std::endl; // Expected output: 14

    return 0;
}
