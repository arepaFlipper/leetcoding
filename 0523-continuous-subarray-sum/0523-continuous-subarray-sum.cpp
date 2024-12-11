#include <vector>
#include <unordered_set>

class Solution {
public:
    bool checkSubarraySum(std::vector<int>& nums, int k) {
      std::vector<int> prefix_sum(nums.size());

      for(int i=0,running_sum=0; i<nums.size();++i){
        running_sum += nums[i];
        running_sum %= k;
        prefix_sum[i] = running_sum;
      }
      std::unordered_set<int> previous;
        
      for(int i=0,running_sum=0; i<nums.size();++i){
        if(previous.find(prefix_sum[i])!= previous.end()){
          return true;
        }

        if(i==0){
          previous.insert(0);
        } else {
          previous.insert(prefix_sum[i-1]);
        }
      }  
      return false;
    }
};
