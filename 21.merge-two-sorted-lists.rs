#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

struct Solution;

impl Solution {
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match (list1, list2) {
            (Some(list1), None) => Some(list1),
            (None, Some(list2)) => Some(list2),
            (None, None) => None,
            (Some(l1), Some(l2)) => {
                if l1.val < l2.val {
                    return Some(Box::new(ListNode {
                        val: l1.val,
                        next: Solution::merge_two_lists(l1.next, Some(l2)),
                    }));
                } else {
                    return Some(Box::new(ListNode {
                        val: l2.val,
                        next: Solution::merge_two_lists(Some(l1), l2.next),
                    }));
                }
            }
        }
    }
}

fn vec_to_list(vec: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;
    for &val in vec.iter().rev() {
        let mut new_node = Box::new(ListNode::new(val));
        new_node.next = current;
        current = Some(new_node);
    }
    current
}

fn list_to_vec(list: Option<Box<ListNode>>) -> Vec<i32> {
    let mut vec = Vec::new();
    let mut current = list;
    while let Some(node) = current {
        vec.push(node.val);
        current = node.next;
    }
    vec
}

// Test functions moved into the global scope
fn test_merge_two_lists_case_1() {
    let list1 = vec_to_list(vec![1, 2, 4]);
    let list2 = vec_to_list(vec![1, 3, 4]);
    let expected = vec![1, 1, 2, 3, 4, 4];
    let result = Solution::merge_two_lists(list1, list2);
    assert_eq!(list_to_vec(result), expected);
    println!("Case 1 succeed 👍")
}

fn test_merge_two_lists_case_2() {
    let list1 = vec_to_list(vec![]);
    let list2 = vec_to_list(vec![]);
    let expected: Vec<i32> = vec![];
    let result = Solution::merge_two_lists(list1, list2);
    assert_eq!(list_to_vec(result), expected);
    println!("Case 2 succeed 👍")
}

fn test_merge_two_lists_case_3() {
    let list1 = vec_to_list(vec![]);
    let list2 = vec_to_list(vec![0]);
    let expected = vec![0];
    let result = Solution::merge_two_lists(list1, list2);
    assert_eq!(list_to_vec(result), expected);
    println!("Case 3 succeed 👍")
}

fn test_merge_two_lists_case_4() {
    let list1 = vec_to_list(vec![5, 10, 15]);
    let list2 = vec_to_list(vec![2, 3, 20]);
    let expected = vec![2, 3, 5, 10, 15, 20];
    let result = Solution::merge_two_lists(list1, list2);
    assert_eq!(list_to_vec(result), expected);
    println!("Case 4 succeed 👍")
}

fn test_merge_two_lists_case_5() {
    let list1 = vec_to_list(vec![2, 3, 7]);
    let list2 = vec_to_list(vec![1, 4, 5]);
    let expected = vec![1, 2, 3, 4, 5, 7];
    let result = Solution::merge_two_lists(list1, list2);
    assert_eq!(list_to_vec(result), expected);
    println!("Case 5 succeed 👍")
}

fn main() {
    // Simulate running tests
    test_merge_two_lists_case_1();
    test_merge_two_lists_case_2();
    test_merge_two_lists_case_3();
    test_merge_two_lists_case_4();
    test_merge_two_lists_case_5();
}
