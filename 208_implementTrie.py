class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.children = {}
        self.debug = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self #其实直接node = self 不如下面新增一个TreeNode()来的雅观啦; 用cur 来代替 node也可
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if self.debug:
            print("Is going to search: ",word)
            print(self.children)
        node = self
        is_exist = True
        for c in word:
            if c not in node.children:
                is_exist = False
                break
            node = node.children[c] #一开始错误的把[] 写成了() 就会报错说dict object is not callable
        return is_exist and node.end
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        is_prefix = True
        for c in prefix:
            if c not in node.children:
                is_prefix = False
                break
            node = node.children[c]
        return is_prefix

'''
    优化1: 用collections.defaultdict来代替{} 
        这样key不存在时，就不会抛出keyerror 而是返回一个默认值
    
'''

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

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

#优化2:  用lambda+reduce 酷炫啊啊啊
#       而且不用is_end 而是用 # 来表示结束
class Trie(object):

    def __init__(self):
        T = lambda: collections.defaultdict(T)
        self.root = T()

    def insert(self, word):
        reduce(dict.__getitem__, word, self.root)['#'] = True

    def search(self, word):
        return '#' in reduce(lambda cur, c: cur.get(c, {}), word, self.root)

    def startsWith(self, prefix):
        return bool(reduce(lambda cur, c: cur.get(c, {}), prefix, self.root))

'''
关于collections 廖雪峰的还挺简洁的 https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456 
关于lambda&reduce 
>>>def add(x, y) :            # 两数相加
...     return x + y
... 
>>> reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
15
>>> reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
15
'''