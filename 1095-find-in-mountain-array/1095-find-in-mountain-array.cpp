/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 */
#include <iostream>
using std::cout;

class MountainArray {
public:
  int get(int index) {
    // Implementation to retrieve the value at the given index
    // Replace this with your actual implementation
    return 0;
  }

  int length() {
    // Implementation to return the length of the array
    // Replace this with your actual implementation
    return 0;
  }
};

class Solution {
private:
  int len;
  int find_peak(MountainArray &mountainArr) {
    int left = 1, right = len - 1; // inclusive, exclusive

    while (left < right) {
      int m = (left + right) / 2;

      int m_val = mountainArr.get(m);
      int m_right = mountainArr.get(m + 1);

      if (m_val < m_right) {
        left = m + 1;
      } else {
        right = m;
      }
    }
    return left;
  }

public:
  int findInMountainArray(int target, MountainArray &mountainArr) {
    len = mountainArr.length();
    int peak = find_peak(mountainArr);

    // binary search on left
    int l = 0, r = peak + 1;
    while (l < r) {
      int m = (l + r) / 2;
      int val = mountainArr.get(m);
      if (val < target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    if (mountainArr.get(l) == target) {
      return l;
    }
    l = peak, r = len;
    while (l < r) {
      int m = (l + r) / 2;
      int val = mountainArr.get(m);

      if (val > target) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    if (l < len && mountainArr.get(l) == target) {
      return l;
    }
    return -1;
  }
};

int main() {
  Solution solution;

  // Example 1
  MountainArray mountainArr1;
  // Set up the mountainArr1 with the provided input array [1,2,3,4,5,3,1]
  int target1 = 3;
  int output1 = solution.findInMountainArray(target1, mountainArr1);
  cout << "Example 1: " << output1 << std::endl; // Expected output: 2

  // Example 2
  MountainArray mountainArr2;
  // Set up the mountainArr2 with the provided input array [0,1,2,4,2,1]
  int target2 = 3;
  int output2 = solution.findInMountainArray(target2, mountainArr2);
  std::cout << "Example 2: " << output2 << std::endl; // Expected output: -1

  return 0;
}
