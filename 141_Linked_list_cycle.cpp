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
    bool hasCycle(ListNode *head) {
        int qpp;
        ListNode *fast, *slow;
        fast = head;
        slow = head;
        bool flag_circle = false;
        while (fast && slow){
            if (slow->next && fast->next && fast->next->next){
                fast = fast->next->next;
                slow = slow->next;
                if (fast==slow){  //一开始位置放错，写在前面了，逻辑bug
                    flag_circle = true;
                    break;
                }
            }
            else break;
        }
        return flag_circle;
    }
};

//竟然看了答案才想起来。 