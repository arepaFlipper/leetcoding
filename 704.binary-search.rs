// @leet start
use std::cmp::Ordering::{Equal, Less, Greater};

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut left, mut right) = (0, nums.len());

        while left < right {
            let mid = left + (right - left ) / 2;
            match target.cmp(&nums[mid]) {
                Equal => return mid as i32,
                Less => right = mid,
                Greater => left = mid + 1,
            }
        }

        -1
    }
}
// @leet end
