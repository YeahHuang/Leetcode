/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 递归 head->next->next = head; head->next = NULL; 
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
    //12.4 重写了一遍 一次AC
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

//36ms 和我最开始的一样 写于10.30 >0.77%
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
    ListNode* reverseList(ListNode* head) {
        ListNode* cur, *tmp;
        if (!head || !head->next) return head;
        cur = head; 
        ListNode tmp1 = ListNode(0);
        if (cur->next == NULL)
            return cur;
        while (cur->next)
        {
            if (cur->next->next)
                cur = cur->next;
            else
            {
                tmp = &tmp1;
                tmp->next = new ListNode(cur->next->val);
                cur->next = NULL;
                tmp->next->next = reverseList(head);
                break;     
        };};
        return tmp1.next;
    };
};