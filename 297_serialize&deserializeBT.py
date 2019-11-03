#referenced from @Stefan 其实不用方向{} 的 你只要能一步步的去弄 而不是 一下子全部 
#类似于我C的 116ms 18.7M
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#My 252ms 21.3M 但其实不用方向{} 的 你只要能一步步的去弄 而不是 一下子全部 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def convert( p):
            return  str(p.val) + "{" + convert(p.left) + "}{"+convert(p.right) + "}"if p else "$"
        return convert(root)
        #self.data = convert(root)
        #print(self.data)
        #return self.data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print("Is deserializing:",data)
        if data == '$':
            return None
        i = 0
        while i<len(data) and data[i]!='{':
            i+=1
        T = TreeNode(int(data[:i]))
        left_start = i + 1
        left_no,i = 1, i+1
        while i<len(data):
            if data[i] == '{':
                left_no += 1
            if data[i] == '}':
                left_no -= 1
                if left_no == 0:
                    break
            i+=1
        #print(left_start, i)
        T.left = self.deserialize(data[left_start:i])
        T.right = self.deserialize(data[i+2: -1])
        return T
         
#用deque的iterative方法 108ms
#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/166904/Python-or-BFS-tm
class Codec:
    def serialize(self, root):    
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res)
                
    
    def deserialize (self, data):
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
        
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))