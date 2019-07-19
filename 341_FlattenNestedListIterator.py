# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList[:]
        
        

    def next(self):
        """
        :rtype: int
        """
        return self.nestedList.pop(0).getInteger()

        '''
        其实就是需要先hasNext 再调用next的 如果都是需要特别判断的话 那么 就没办法保证next一定返回int了吖
        看清楚下面的demo code才好
        if self.nestedList.isInteger():
            return self.nestedList.getInteger()
        else:
            return self.next(self.nestedList.getList())
        '''


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.nestedList:
            top = self.nestedList[0]
            if top.isInteger():
                return True
            self.nestedList = top.getList() + self.nestedList[1:]
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())