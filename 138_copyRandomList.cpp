/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        RandomListNode *ret, *cur=head;
        unordered_map<RandomListNode*, RandomListNode*> map;
        while (cur){
            RandomListNode* node = new RandomListNode(cur->label);
            map[cur] = node;
            cur = cur->next;
        }
        cur = head;
        while (cur){
            RandomListNode* node = map[cur];
            node -> next = map[cur->next];
            node -> random = map[cur->random];
            cur = cur->next;
        }
        ret = map[head];
        return ret;
    }
};

// yes! 背诵正确！ 但是为什么？ 不能直接一遍push即可？
