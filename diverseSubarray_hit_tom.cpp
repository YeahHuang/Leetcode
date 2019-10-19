//#include <bits/stdc++.h>
/*#include "/Users/huangxiao/Downloads/stdc++.h"

#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <tgmath.h>*/
//#include <iostream>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <cmath>
//#include <tgmath.h>
using namespace std;

#define ll long long
#define pii pair<int, int>
#define pb push_back
#define pli pair<ll, int>
#define pil pair<int, ll>
#define clr(a, x) memset(a, x, sizeof(a))

const double pi = acos(-1.0);
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const double EPS = 1e-9;

int q,p1,p2,ans,T, n, s, a[100015], b[100015], rec[100015],ma[400015], lazy[400015];
vector<int> m[100015];

void pushdown(int i){
    if (lazy[i]){
        ma[i<<1] += lazy[i];
        ma[i<<1|1] += lazy[i];
        lazy[i<<1] += lazy[i];
        lazy[i<<1|1] += lazy[i];
        lazy[i] = 0;
    }
}

void pushup(int i){
    ma[i] = max(ma[i<<1|1], ma[i<<1]);
}

void update(int i, int l, int r, int x, int y,int value){
    if (x<=l && r<=y){
        ma[i] += value;
        lazy[i] += value;
    }
    else{
        pushdown(i);
        int mid = l + r >> 1;
        if (x<=mid) update(i<<1, l, mid, x,y,value);
        if (y>=mid+1) update(i<<1|1, mid+1, r, x, y,value);
        /*
        if (y<=mid) update(i<<1, l, mid, x,y,value);
        else if (x>=mid+1) update(i<<1|1, mid+1, r, x, y, value);
        else{
            update(i<<1, l, mid, x, mid, value);
            update(i<<1|1, mid+1, r, mid+1, y, value);
        }*/
        pushup(i);
    }
}

void build(int i, int l, int r){
    lazy[i] = 0;
    if (l == r){
        ma[i] = b[l];
    }else
    {
        int mid = (l+r) >> 1;
        build(i<<1, l, mid);
        build(i<<1|1, mid+1, r);
        pushup(i);
    }
}

int query(int i, int l, int r, int x, int y){
    int res = 0;
    if (x<=l && r<=y)
        res = ma[i];
    else{
        pushdown(i);
        int mid = (l+r) >> 1;
        if (x<=mid) res = query(i<<1, l, mid, x,y);
        if (y>=mid+1) res = max(res,query(i<<1|1, mid+1, r, x, y));
        //pushup(i);
        /*else{
            res = query(i<<1, l, mid, x, mid);
            res = max(res, query(i<<1|1, mid+1, r, mid+1, y));
        }*/
    }
    return res;
}

int main(){
    scanf("%d",&T);
    for (int it=0;it<T; it++){
        scanf("%d%d",&n,&s);
        clr(b,0); for(int i=1; i<=100000;i++) m[i].clear();
        for (int i=1;i<=n;i++){
            scanf("%d",&a[i]);
            m[a[i]].pb(i);
            rec[i] = m[a[i]].size();
            if (rec[i]<=s) b[i]=b[i-1]+1;
            else if (rec[i]==s+1) b[i] = b[i-1]-s;
                            else b[i] = b[i-1];
        }
        for (int i=1;i<=100000;i++) m[i].pb(n+1);
        build(1,1,n);
        ans = 0;
        for (int l=1; l<=n; l++){
            q = query(1,1,n,l,n);
            //for (int j=1; j<=n*2; j++) printf("%d ",ma[j]);printf("\n");
            //for (int j=1; j<=n*2; j++) printf("%d ",lazy[j]);printf("\n");  
            //printf("q=%d\n",q);
            ans = max(ans,q);
            if (rec[l] + s < (int)m[a[l]].size()) {
                int x = rec[l] + s - 1;
                update(1,1,n,l,m[a[l]][x] - 1, -1);
                update(1,1,n, m[a[l]][x], m[a[l]][x+1]-1, s);
            } else
                {update(1,1,n,l,n,-1);}
        }

        printf("Case #%d: %d\n",it+1, ans);
    }
}