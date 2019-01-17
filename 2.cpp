/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode *q = &head;  // 这里用curr更清晰
        int carry, sum, p1, p2;
        carry = 0;
        
        while ( l1 || l2 || carry){
            p1 = l1 ? l1->val:0;
            p2 = l2 ? l2->val:0;
            sum = p1 + p2 + carry; // 可改为 sum = (l1?l1->val:0) + (l2?l2->val:0) + carry
            carry = sum / 10;       //可改为 carry = sum>9 ? 1:0; 这样更快
            sum = sum % 10;
            q -> next = new ListNode(sum);
            q = q->next;
            l1 = l1 ? l1 -> next : l1;
            l2 = l2 ?  l2 -> next : l2;
    }
        return head.next;
};