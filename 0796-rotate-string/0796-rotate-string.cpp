class Solution {
public:
  bool rotateString(string s, string goal) {
    for (int rotations = 0; rotations < s.length(); rotations++) {
      if (s == goal) {
        return true;
      }

      // do a single rotation
      for (int i = 0; i < s.length() - 1; i++) {
        swap(s[i], s[i + 1]);
      }
    }
    return false;
  }
};
