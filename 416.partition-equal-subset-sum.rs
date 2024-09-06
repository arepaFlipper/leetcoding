// @leet start
use std::collections::HashSet;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let sum: i32 = nums.iter().sum();
        if sum % 2 != 0 {
            return false;
        }

        let target = sum/2;
        let mut dp = HashSet::new();
        dp.insert(0);

        for num in nums {
            let mut next_dp = HashSet::new();
            for &t in &dp {
                if t + num == target {
                    return true;
                }
                next_dp.insert(t+num);
                next_dp.insert(t);
            }
            dp = next_dp;
        }

        false
    }
}
// @leet end
