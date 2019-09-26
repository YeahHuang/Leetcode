class Vector2D:
    #但我其实有点针对性了的在排坑 anyway
    def __init__(self, v: List[List[int]]):
        self.v = v[::-1]

    def next(self) -> int:
        l = self.v.pop()
        if len(l) > 1:
            self.v.append(l[1:])
        return l[0]

    def hasNext(self) -> bool:
        if len(self.v)==0:
            return False
        l = self.v.pop()
        if not(l==[] or ((type(l) == type([]) and type(l[0])==type([])))):
            self.v.append(l)
            return True
        return self.hasNext()


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#C++ @Stephan
class Vector2D {
    vector<vector<int>>::iterator i, iEnd;
    int j = 0;
public:
    Vector2D(vector<vector<int>>& vec2d) {
        i = vec2d.begin();
        iEnd = vec2d.end();
    }

    int next() {
        hasNext();
        return (*i)[j++];
    }

    bool hasNext() {
        while (i != iEnd && j == (*i).size())
            i++, j = 0;
        return i != iEnd;
    }
};