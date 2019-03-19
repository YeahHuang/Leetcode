T = int(input())
for i in range(T):
    qpp = input().split(" ")
    k = int(qpp[0])
    v = int(qpp[1])
    ans = 0 

    if k<2*v:
        for r in range(k+1):
            for g in range(max(0, r-v), min(k,r+v)+1):
                ans += min(k,min(r,g)+v) - max(0,max(r,g)-v) + 1
    else:
        for r in range(v):
            for g in range(0, r+v+1):
                ans += min(k,min(r,g)+v) - max(0,max(r,g)-v) + 1
        ans *= 2
        ans += (3*v*(v+1)+1) * (k-2*v+1)
  
    print("Case #%d: %s"%(i+1, ans)) #应该可以继续推公式 或者相对关系也行。 很接近了应该