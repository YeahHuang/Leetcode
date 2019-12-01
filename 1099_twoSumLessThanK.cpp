/*
class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        int l,r;
        l = 0;
        r = A.size() - 1 ;
        int maxi = -1;
        while (l<r){
            while ((l<r) && (A[l]+A[r]>=K))
                r -= 1;
            if (l<r)
                maxi = max(maxi, A[l]+A[r]);
            l += 1;
        }
        return maxi;
    }
};*/
class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        int S=-1,sum=0;
        sort(A.begin(),A.end());
        int i=0,j=A.size()-1;
        while(i<j)
        {
            if(A[i]+A[j]<K)
                S=max(S,A[i++]+A[j]);
            else
                j--;
        }
        return S;
    }
};