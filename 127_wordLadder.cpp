#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) { //656ms faster than 15%
        int q,p1,p2,l1,l2,r1,r2,n,curLen1, curLen2, ladderLen = 0;
        unordered_map<int, vector<int>> hash;
        vector<int> curFromBegin, curFromEnd; //考虑在其中/不在其中的2种。
        vector<int> fatherBegin, fatherEnd;
        vector<int> lengthBegin, lengthEnd;
        vector<string>::iterator it;
        bool minusBegin = false;
        bool minusEnd = false;
        //it = find(wordList.begin(), wordList.end(),beginWord); if (it!=wordList.end()) {minusBegin = true; } 
        it = find(wordList.begin(), wordList.end(),endWord); if (it!=wordList.end()) {minusEnd = true; }

        if (minusEnd && compare(beginWord, endWord)) ladderLen = 1;
        if (minusEnd && !wordList.empty()){
        n = wordList.size();
        unordered_map<int,bool> flagBegin, flagEnd;
        for (int i=0;i<n;i++){flagEnd[i]=false;flagBegin[i]=false;};
        //一开始写的 wordList.find(beginWord)了 注意这是map的用法
        
        
        if (debug) {
            printf("minusBegin:%d minusEnd:%d n=%d\n",minusBegin, minusEnd, n);
            if (n>2) printf("%s", wordList[2]);
        }
        len = wordList[0].size();
        for (int i=0; i<n; i++)
            for (int j=i+1; j<n; j++)
                if (compare(wordList[i],wordList[j])){
                    hash[i].push_back(j);
                    hash[j].push_back(i);
                    if (debug) printf("[%d,%d] ", i, j);
                }
        //printf('\n');
        for (int i=0;i<n;i++){
            if (compare(beginWord, wordList[i])) { //注意if后的条件要加括号！一开始忘了
                curFromBegin.push_back(i);
                fatherBegin.push_back(-1);
                lengthBegin.push_back(1);
                flagBegin[i]=true;
            }
            if (compare(endWord, wordList[i])) {
                curFromEnd.push_back(i);
                fatherEnd.push_back(-1);
                lengthEnd.push_back(1);
                flagEnd[i]=true;
                if (flagBegin[i]) {ladderLen = 2;break;}
            }
        };
        l1 = l2 = 0; //一开始忘记声明l1 l2 r1 r2
        if (minusEnd && !curFromBegin.empty() && !curFromEnd.empty()) {
            r1 = curFromBegin.size()-1; r2 = curFromEnd.size()-1;
            if (compare(beginWord,endWord)) ladderLen = 1;
        } 
        else {r1 = r2 = -1;}

        if (debug){
            printf("\ncurFromBe: ");for (int i=0;i<=r1;i++) printf("\t%d",curFromBegin[i]);
            printf("\nfatherBegin: "); for (int i=0;i<=r1;i++) printf("\t%d",fatherBegin[i]);
            printf("\nlengthBegin: ");for (int i=0;i<=r1;i++) printf("\t%d",lengthBegin[i]);
            printf("\ncurFromEnd: ");for (int i=0;i<=r2;i++) printf("\t%d",curFromEnd[i]);
            printf("\nfatherEnd: "); for (int i=0;i<=r2;i++) printf("\t%d",fatherEnd[i]);
            printf("\nlengthEnd: ");for (int i=0;i<=r2;i++) printf("\t%d",lengthEnd[i]);
            printf("\n");
        }    
        
        while (!ladderLen && l1<=r1 & l2<=r2){
            curLen1 = lengthBegin[l1]+1;
            while (l1<=r1 && lengthBegin[l1]+1==curLen1){
                p1 = curFromBegin[l1];  
                if (debug) {
                    for (int idx: hash[p1]) printf("%d ",wordList[idx]);
                    printf("\nl1=%d, r1=%d, p1=%d, curLen1=%d\n",l1,r1, p1,curLen1);
                }
                for (int idx: hash[p1])
                    if (flagEnd[idx]) {ladderLen = curLen1 + lengthEnd.back(); break;}//一开始这里新加了分号； 注意c++里 if如果要连接else不用加分号
                    else if (!flagBegin[idx]){
                        curFromBegin.push_back(idx);
                        fatherBegin.push_back(l1);
                        lengthBegin.push_back(curLen1);
                        flagBegin[idx] = true;
                        r1++;
                    }
                l1 ++;
            }
            if (ladderLen) break;
            if (debug){
            printf("curFromBe: ");for (int i=0;i<=r1;i++) printf("\t%d",curFromBegin[i]);
            printf("\nfatherBegin: "); for (int i=0;i<=r1;i++) printf("\t%d",fatherBegin[i]);
            printf("\nlengthBegin: ");for (int i=0;i<=r1;i++) printf("\t%d",lengthBegin[i]);
            printf("\n");
            }

            curLen2 = lengthEnd[l2]+1;
            while (l2<=r2 && lengthEnd[l2]+1==curLen2){
                p2 = curFromEnd[l2]; 
                if (debug) {
                    for (int idx: hash[p2]) printf("%d ",idx);
                    printf("\nl2=%d, r2=%d, p2=%d, curLen2=%d\n",l2,r2, p2,curLen2);
                }
                for (int idx: hash[p2])
                    if (flagBegin[idx]) {ladderLen = curLen2 + lengthBegin.back(); break;}//成啦！
                    else if (!flagEnd[idx]){
                            curFromEnd.push_back(idx);
                            fatherEnd.push_back(l2);
                            lengthEnd.push_back(curLen2);
                            flagEnd[idx] = true;
                            r2++;
                        };
                l2 ++; 
            }
            

            if (debug){
            printf("curFromEnd: ");for (int i=0;i<=r2;i++) printf("\t%d",curFromEnd[i]);
            printf("\nfatherEnd: "); for (int i=0;i<=r2;i++) printf("\t%d",fatherEnd[i]);
            printf("\nlengthEnd: ");for (int i=0;i<=r2;i++) printf("\t%d",lengthEnd[i]);
            printf("\n");
            }
        }
        if (ladderLen) ladderLen+=1; }
        return ladderLen;
    }
private:
    bool compare(string s1, string s2){ //already assumed no same 2 words.
        int dif_num = 0;
        if (s1.size()!=s2.size()) cout<<"ERROR! len1 != len2."<<endl;
        for (int i=0;i<len;i++)
            if (s1[i]!=s2[i]){
                dif_num += 1;
                if (dif_num>1) break;
            }
        if (dif_num==0) dif_num = 2;
        //if (debug) printf("s1=%s, s2=%s, dif_num=%d\n",s1.c_str(),s2.c_str(), dif_num);
        return (dif_num>1)?false:true;
    }

    vector<vector<string>> findPath(int idx, vector<int> father,  vector<int> cur){
        vector<vector<string>> path; //可以考虑合并
        while (father[idx]!=-1){
            //path.push_back(cur[idx]);
            idx = father[idx];
        }
        return path; 
    }

    int len = 0; 
    bool debug = true;

    //['abc','acd']

    //["aa","ac","ca","ad","da", "bb"]     aa bb
};


/*RE in ['hot','dog'] hot dog
/WA in "cat"
"fin"
["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep",
"tug","ump","arc","fee",
"lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe",
"pis","dot","jaw","hat","roe","ada","mac"]*/