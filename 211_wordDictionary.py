class WordNode:
    def __init__(self):
        self.children = collections.defaultdict(WordNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str, cur=None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if cur is None:
            cur = self.root
        is_exist, flag = True, False
        for i, c in enumerate(word):
            if c=='.':
                flag = False
                for child in cur.children:
                    if self.search(word[i+1:], child):
                        flag = True
                        break
                is_exist = flag
                break
            else:
                cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
                if cur is None:
                    is_exist = False
                    break
        if is_exist and flag==False and cur.end==False:
            is_exist = False
        return is_exist


class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        cur = self.root
        is_exist = True
        for c in word:
            cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
            if cur is None:
                is_exist = False
                break
        return is_exist and cur.end

    def startsWith(self, prefix):
        cur = self.root
        is_prefix = True
        for c in prefix:
            cur = cur.children.get(c) #这里为了判定是否为空 由直接新建 -> .get 函数 注意一下
            if cur is None:
                is_prefix = False
                break
        return is_prefix