/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
class Solution { //Divide&Conquer大法好。 NlogK  32ms > 46.64% 没有尝试k最小堆 复杂度一样的 以后有机会试一下。
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int qpp = (int) lists.size();  //vector<ListNode*>& 不要被这个弄怕了呀！ 只要是vector就可以.size
        ListNode* ans = NULL;
        if (qpp>0) ans = doMerge(lists, 0, qpp-1);
        return ans;
    }

    ListNode* doMerge(vector<ListNode*>& lists, int left, int right) {
        ListNode* ret=NULL;
        if (left > right) {
            printf("ERROR! left=%d > right=%d",left, right); //一开始这个顺序和下面写反了 一下子都是error！
        } 
        else
            if (left==right) ret = lists[left];
            else {
                int mid = (left + right)/2;
                ret = mergeTwoLists(doMerge(lists, left, mid), doMerge(lists, mid+1, right));
            }
        return ret;    
    }


    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode *cur = &head;
        while ( l1 && l2 ) {
            if (l1->val < l2->val)
            {
                cur -> next = new ListNode(l1->val);
                cur = cur->next;
                l1 = l1->next;
            }else
            {
                cur -> next = new ListNode(l2->val);
                cur = cur->next;
                l2 = l2->next;
            }
        }
        if (l1) cur -> next = l1;
        if (l2) cur -> next = l2;
        return head.next;
    }
};


