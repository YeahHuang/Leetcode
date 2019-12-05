/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/*
We can recursively define the result of a merge operation on two lists as the following

We model the above recurrence directly, first accounting for edge cases. Specifically, if either of l1 or l2 is initially null, there is no merge to perform, so we simply return the non-null list. Otherwise, we determine which of l1 and l2 has a smaller head, and recursively set the next value for that head to the next merge result.

*/

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head, *cur;
        head = new ListNode(0);
        cur = head;
        for (l1, l2; l1!=NULL or l2!=NULL; )
        {
            if (l1==NULL || (l2!=NULL && l1->val > l2->val)){  //一开始自作聪明合并 忘记判断l2是否为NULL
                cur->next = new ListNode(l2->val);
                cur = cur->next;
                l2 = l2->next;
            } else {
                cur->next  = new ListNode(l1->val); //一开始写成了==
                cur = cur->next;
                l1 = l1->next;
            }
        }
        return head->next;
    }
};