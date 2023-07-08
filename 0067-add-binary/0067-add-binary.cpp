class Solution {
public:
  string addBinary(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    string c = "";

    while (a.length() < b.length()) {
      a.push_back('0');
    }

    while (b.length() < a.length()) {
      b.push_back('0');
    }

    int carry = 0;

    for (int i = 0; i < a.length() || carry > 0; ++i) {
      int cur = carry;
      if (i < a.length()) {
        cur += a[i] - '0';
        cur += b[i] - '0';
      }
      int rem = cur % 2;
      carry = cur / 2;

      c.push_back(rem + '0');
    }
    reverse(c.begin(), c.end());
    return c;
  }
};
