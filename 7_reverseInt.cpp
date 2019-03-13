class Solution {
public:
    int reverse(int x) {
        bool flagNeg = false;
        bool flagInvalid = false;
        int reverseInt = 0;
        if (x<0) 
            if (x!=INT_MIN) {
                x *= -1;
                flagNeg = true;
            } else
                flagInvalid = true;
        if (debug) printf("%d  ",flagNeg);
        if (flagInvalid==false)
        while (x>0){
            if ((INT_MAX - x%10)/10<reverseInt)
            {
                flagInvalid = true;
                break;
            }
            reverseInt = reverseInt * 10 + x % 10;
            x = x / 10;
        }

        if (flagInvalid) reverseInt = 0;
        else
            if (flagNeg) reverseInt *= -1;
        return reverseInt;

    } //一开始没有好好的考虑overflow的问题 1534236469 的时候WA了一次 

private:
    bool debug = true;
};