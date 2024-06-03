I want you to write the tests to my code in the same manner you've been doing early in this chat, here is my problem:

             https://leetcode.com/problems/merge-two-sorted-lists/
                                        
                           21. Merge Two Sorted Lists
                    Easy  │ 21563  2099  │ 64.4% of 6.5M



You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



󰛨 Example 1:

[img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

	│ Input: list1 = [1,2,4], list2 = [1,3,4]
	│ Output: [1,1,2,3,4,4]

󰛨 Example 2:

	│ Input: list1 = [], list2 = []
	│ Output: []

󰛨 Example 3:

	│ Input: list1 = [], list2 = [0]
	│ Output: [0]



 Constraints:

	* The number of nodes in both lists is in the range [0, 50].
	
	* -100 <= Node.val <= 100
	
	* Both list1 and list2 are sorted in non-decreasing order.






The following is my solution to test:

```rust
// @leet start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match (list1, list2){
            (Some(list1), None)=> Some(list1),
            (None, Some(list2))=> Some(list2),
            (None, None)=> None,
            (Some(l1), Some(l2)) => {
                if l1.val<l2.val {
                    return Some(Box::new(ListNode{val: l1.val, next:Solution::merge_two_lists(l1.next,Some(l2))}));
                } else {
                    return Some(Box::new(ListNode {val: l2.val, next: Solution::merge_two_lists(Some(l1),l2.next) }))
                }
            }
        }
    }
}
// @leet end
```
