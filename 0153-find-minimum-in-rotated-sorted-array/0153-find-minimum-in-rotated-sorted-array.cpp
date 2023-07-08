class Solution {
public:
  int findMin(vector<int> &nums) {
    int l = 0, r = nums.size();
    if (nums[l] <= nums[r - 1]) {
      // Array is not rotated at all.
      return nums[l];
    }

    while (l < r) {
      int mean = (l + r) / 2;
      if (nums[mean] >= nums[0]) {
        l = mean + 1;
      } else {
        r = mean;
      }
    }
    return nums[l];
  }
};
