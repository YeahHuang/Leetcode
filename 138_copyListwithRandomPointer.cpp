/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/

/*RandomListNode *copyRandomList(RandomListNode *head) {
    RandomListNode *newHead, *l1, *l2;
    if (head == NULL) return NULL;
    for (l1 = head; l1 != NULL; l1 = l1->next->next) {
        l2 = new RandomListNode(l1->label);
        l2->next = l1->next;
        l1->next = l2;
    }
        
    newHead = head->next;
    for (l1 = head; l1 != NULL; l1 = l1->next->next) {
        if (l1->random != NULL) l1->next->random = l1->random->next;
    }
        
    for (l1 = head; l1 != NULL; l1 = l1->next) {
        l2 = l1->next;
        l1->next = l2->next;
        if (l2->next != NULL) l2->next = l2->next->next;
    }

    return newHead;
}
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head==NULL) return NULL; //WA2 一开始忘记写了
        
        Node *newHead, *l1, *l2;
        for (l1=head; l1!=NULL; l1=l1->next->next)
        {
            l2 = new Node(l1->val, NULL, NULL);
            l2->next = l1->next;
            l1->next = l2;
        }
        
        
        
       /* for (l1=head; l1!=NULL; l1=l1->next->next){
            if (l1->random!=NULL)
                l1->next->random = l1->random->next;
        }*/
        

        newHead = head->next;
        for (l1=head; l1!=NULL; l1=l1->next->next){
            l2 = l1->next; //同时删减会bug 会只剩多一个 指针 
            //if (l1->next->next) l2->next = l1->next->next->next; //把链表结构改了呀 难怪WA了
            if (l1->random) l2->random = l1->random->next;
        }
        
        for (l1=head; l1!=NULL; ){
            Node *tmp = l1->next->next; //tmp could be NULL!!!!!
            l2 = l1->next;
            if (tmp) l2->next = tmp->next;   //tmp->next or l2->next->next             
            l1->next = tmp;
            l1 = tmp;
        }
        
        return newHead;
    }
};