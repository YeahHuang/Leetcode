class Solution {
public:
    /*int countPrimes(int n) {
        int cnt = 0;
        if (n>2){                  //228ms faster than 23.73%
            primes.push_back(2);
            for (int i=3; i<n; i++)
                if (judgePrime(i)) primes.push_back(i);
            cnt = primes.size();
        }
        return cnt;
    }*/

    int countPrimes(int n) {
        int t,qpp,cnt = 0;
        int sqrt_n = int(sqrt(n));//12ms faster than 98.55%
        vector<bool> isPrime(n,true); 
        qpp = n; //without qpp 16ms
        if (n>2){ 
            cnt++;
            for (int i=3; i<n; i+=2) //trick1  i+=2; 
                if (isPrime[i]){
                    cnt++;          //trick2 cnt++ along the way
                    if (i<=sqrt_n){
                        t = 2*i; //use t to replace 2*i is unuseful
                        for (int j=i*i; j<n; j+=2*i) //tricks 3&4 j=i*i & j+=2*i 
                            isPrime[j] = false;
                    } else {qpp = i+2; break;} //一开始写成了qpp = i+1; 
                };
            for (int i=qpp; i<n; i+=2)  //trick5 avoid additional add;
                if (isPrime[i]) cnt++;
            }
        return cnt;
    }

private:
    vector<int> primes;

    bool judgePrime(int qpp){
        bool isPrime = true;
        int sqrt_qpp = int(sqrt(qpp));
        for (int prime: primes){
            if (prime>sqrt_qpp) break;
            if (qpp%prime==0) {isPrime = false; break;};
        }
        return isPrime;
    }
};