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
    /*ListNode* reverseList(ListNode* head) {
        ListNode revHead(0);
        ListNode* revList = &revHead;
        if (debug) cout<<0<<head->val<<endl;
        if (!head) {
            ListNode* head0 = new ListNode(head->val);
            if (debug) cout<<1<<head->val<<endl;
            if (!head->next) {
                if (debug) cout<<head->val<<endl;
                revList->next = reverseList(head->next);
                while (!revList->next) revList = revList->next; //必须!(revList->next)不加括号不对！
                revList->next = head0;
            }               
            else revList->next = head0;
        }
        return revHead.next;
    }*/
    ListNode* reverseList(ListNode* head) { //12ms
        //ListNode revHead(0);
        ListNode *cur, *prev=NULL;
        cur = head;
        while (cur!=NULL){
            ListNode *tempNext = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tempNext;
        }
        return prev;
    }

    ListNode* reverseList(ListNode* head) { //8ms
        ListNode *revList;
        if ( !head || !(head->next)) revList = head;
        else
        {
            revList = reverseList(head->next);
            head->next->next = head;
            head->next = NULL;
        }
        return revList;
    }


private:
    bool debug = true;
};

//36ms >0.77%