#Sol1 my 1388ms
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insertAndJudge(self, word):
        cur = self.root
        is_concatenated_word = False
        for i,c in enumerate(word):
            if cur.end and is_concatenated_word == False:
                if self.search(word[i:]):
                    is_concatenated_word = True
            cur = cur.children[c]
        cur.end = True
        return is_concatenated_word

    def search(self, word):
        cur = self.root
        is_exist = True
        ret = False
        for i,c in enumerate(word): #maximum recursion 
            if cur.end and i:
                if self.search(word[i:]):
                    ret = True
                    break
            cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
            if cur is None:
                is_exist = False
                break 
        if is_exist and cur.end:
            ret = True
        return ret


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        words.sort(key = lambda x: len(x))
        ret = []
        for w in words:
            flag = trie.insertAndJudge(w)
            if flag:
                ret.append(w)
        return ret #WA2 debug了超级久 竟然发现返回为空的原因是忘记写 return ret了c

#440ms 有时候直接哈希更快～
class Solution(object): 
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True

            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res