/**
 * Definition for singly-linked list.
 */
#include <iostream>
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    ListNode *head = nullptr;
    ListNode *tail = nullptr;

    while (list1 != nullptr || list2 != nullptr) {
      ListNode *cur = new ListNode();
      if (list1 == nullptr) {
        cur->val = list2->val;
        list2 = list2->next;
      } else if (list2 == nullptr) {
        cur->val = list1->val;
        list1 = list1->next;
      } else {
        if (list1->val <= list2->val) {
          cur->val = list1->val;
          list1 = list1->next;
        } else {
          cur->val = list2->val;
          list2 = list2->next;
        }
      }

      if (head == nullptr)
        head = cur;
      if (tail == nullptr) {
        tail = cur;
      } else {
        tail->next = cur;
        tail = cur;
      }
    }
    return head;
  }
};

int main() {
  // Create two linked lists for testing
  ListNode *list1 = new ListNode(1);
  list1->next = new ListNode(3);
  list1->next->next = new ListNode(5);

  ListNode *list2 = new ListNode(2);
  list2->next = new ListNode(4);
  list2->next->next = new ListNode(6);

  Solution solution;

  // Merge the two lists
  ListNode *mergedList = solution.mergeTwoLists(list1, list2);

  // Print the merged list
  ListNode *cur = mergedList;
  while (cur != nullptr) {
    std::cout << cur->val << " ";
    cur = cur->next;
  }
  std::cout << std::endl;

  // Clean up the memory
  cur = mergedList;
  while (cur != nullptr) {
    ListNode *temp = cur;
    cur = cur->next;
    delete temp;
  }

  // Clean up the memory for the original lists
  cur = list1;
  while (cur != nullptr) {
    ListNode *temp = cur;
    cur = cur->next;
    delete temp;
  }

  cur = list2;
  while (cur != nullptr) {
    ListNode *temp = cur;
    cur = cur->next;
    delete temp;
  }

  return 0;
}
