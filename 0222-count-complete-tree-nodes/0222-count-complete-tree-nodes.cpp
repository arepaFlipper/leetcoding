/**
 * Definition for a binary tree node.
 */
/* struct TreeNode { */
/*   int val; */
/*   TreeNode *left; */
/*   TreeNode *right; */
/*   TreeNode() : val(0), left(nullptr), right(nullptr) {} */
/*   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} */
/*   TreeNode(int x, TreeNode *left, TreeNode *right) */
/*       : val(x), left(left), right(right) {} */
/* }; */

class Solution {
private:
  bool exists(int target, int d, TreeNode* root) {
    for (int i = 0; i < d; ++i) {
      int bit = (d - 1) - i;
      if((target >> bit) & 1){
        root = root -> right;
      } else {
        root = root -> left;
      }
    }
    return root != nullptr;
  }

public:
  int countNodes(TreeNode* root) {
    if (root == nullptr) {
      return 0;
    }

    int depth = 0;
    TreeNode* depth_seeker = root;
    while (depth_seeker -> left != nullptr) {
      depth++;
      depth_seeker = depth_seeker->left;
    }
 

    int l = 0, r = (1 << depth);
    while (l < r) {
      int m = (l + r) / 2;

      if (exists(m,depth,root)) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    return (1 << depth) - 1 + l;
  }
};
