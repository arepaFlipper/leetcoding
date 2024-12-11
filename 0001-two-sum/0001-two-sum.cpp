#include <iostream>
#include <vector>
class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::vector<int> ans;
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] + nums[j] == target) {
          ans.push_back(i);
          ans.push_back(j);
          return ans;
        }
      }
    }
    return ans;
  }
};

int main() {
  Solution solution;
  std::vector<int> nums1 = {2, 7, 11, 15};
  int target = 26;
  std::vector<int> example1 = solution.twoSum(nums1, target);
  std::cout << "example1: ";
  for (int i = 0; i < example1.size(); i++) {
    std::cout << example1[i] << " ";
  }
  std::cout << std::endl;
  if (example1 == std::vector<int>{0, 1}) {
    std::cout << "good " << std::endl;
  } else {
    std::cout << "not good" << std::endl;
  }
}
