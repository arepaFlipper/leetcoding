/**
 * Definition for a binary tree node.
#include <algorithm>
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

class Solution {
public:
  // returned value is (a) - largest verical path going through current
  int answer;
  int findAB(TreeNode *current) {
    if (current == nullptr){
      return 0;
    }

    // find a
    int left = findAB(current -> left);
    int right = findAB(current -> right);

    //starting from {this node, this node + left, this node + right }
    int a_value = std::max({ current->val, current->val + left, current-> val + right });

    if (left <0) {
      left = 0;
    }

    if (right <0) {
      right = 0;
    }

    int b_value = current -> val + left + right;

    answer = max(b_value, answer);
    return a_value;
  }
  int maxPathSum(TreeNode *root) {
    answer = -1e9;
    findAB(root);

    return answer;
  }
};

