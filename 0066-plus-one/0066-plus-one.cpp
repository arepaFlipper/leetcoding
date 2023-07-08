class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
      bool all_9 = true;
      for(int x: digits){
        // in case of 999999
        if (x != 9){
          all_9 = false;
        }else{
          // Don nothing
        }
      }
      if (all_9){
        digits.insert(digits.begin(),0);
        for (int& x: digits) x = 0;
        digits[0] = 1;
      } else {
        for (int i = digits.size()-1; i >= 0; i--){
          digits[i]++;
          if(digits[i] == 10){
            // carrier
            digits[i]=0;
          } else {
            break;
          }
        }
      }
      return digits;
    }
};
