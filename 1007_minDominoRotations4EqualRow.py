class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ret = min(self.min4A(A, B), self.min4A(B, A))
        return ret if ret!=len(A)+1 else -1 
        
    def min4A(self, A, B):
        min_rotations = len(A) + 1
        c_a = collections.Counter(A)
        key, cnt = sorted(c_a.items(), key = lambda x: x[1])[-1]
        if cnt >= len(A) // 2:
            flag, rot = True, 0
            for i in range(len(A)):
                if A[i]!=key:
                    if B[i]!=key:
                        flag = False
                        break
                    else: 
                        rot += 1
            if flag:
                min_rotations = rot
        return min_rotations

    #官方的solution 利用a[0] b[0]中必有一个会作为key 可以有一个不用counter的Improvement 1364ms->1336ms
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotations_a += 1   
                elif B[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0]) 
        if rotations != -1 or A[0] == B[0]:
            return rotations 
        else:
            return check(B[0])