/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
      ListNode* head = nullptr;
      ListNode* tail = nullptr;

      while (list1 != nullptr || list2 != nullptr){
        ListNode* cur = new ListNode();
        if (list1 == nullptr) {
          cur->val = list2->val;
          list2 = list2->next;
        } else if (list2 == nullptr){
          cur->val = list1->val;
          list1 = list1->next;
        } else {
          if (list1->val <= list2->val){
            cur->val = list1->val;
            list1 = list1->next;
          } else {
            cur->val = list2->val;
            list2 = list2->next;
          }
        }

        if (head == nullptr) head = cur;
        if (tail == nullptr){
          tail = cur;
        } else {
          tail->next = cur;
          tail = cur;
        }
      }
      return head;
    }
};
