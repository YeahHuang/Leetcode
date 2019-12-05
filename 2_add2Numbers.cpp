/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/*
Intuition

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.


*/
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *cur, *head;
        head = new ListNode(0);
        cur = head;
        int sum, carry = 0;
        for (l1, l2; l1!=NULL or l2!=NULL;){
            if (l1!=NULL && l2!=NULL){
                sum = l1->val + l2->val + carry;
                l1 = l1->next;
                l2 = l2->next;
            } else if (l1!=NULL){
                sum = l1->val + carry;
                l1 = l1->next;
            } else{
                sum = l2->val + carry;
                l2 = l2->next;
            }
            cur->next = new ListNode(sum%10);
            carry = sum / 10; 
            cur = cur->next;
        }
        if (carry != 0)
            cur -> next = new ListNode(carry);
        return head->next;
    }
};