/**
 * Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};
 */
#include <algorithm>
#include <utility>

class Solution {
private:
  int answer;
  std::pair<int, int> dp(TreeNode *cur) {
    // first -> dp(cur,0)
    // second -> dp(cur,1)
    if (cur == nullptr) {
      return {0, 0};
    }
    std::pair<int, int> ret;
    std::pair<int, int> left = dp(cur->left);
    std::pair<int, int> right = dp(cur->right);

    int best_left = std::max(left.first, left.second);
    int best_right = std::max(right.first, right.second);

    ret.first = best_left + best_right;
    ret.second = left.first + right.first + cur->val;

    answer = std::max({answer, ret.second, ret.first});
    return ret;
  }

public:
  int rob(TreeNode *root) {
    answer = 0;
    dp(root);
    return answer;
  }
};
