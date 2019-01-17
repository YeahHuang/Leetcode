#define INT_MAX 2147483647 // 如果是c++则不用写
#define INT_MIN -2147483648
int myAtoi(char* str) {
    bool neg = false;  //false是全小写 
        long long ans = 0;  //一开始写int 会在极值出错
        for (;isspace(*str);str++); //isspace isdigit 这个很巧妙。 
        if (*str == '+' || *str == '-'){
            neg = (*str=='-');
            str++;
        }            
        while (isdigit(*str)){
            if  (!neg && *str - '0' > INT_MAX - ans * 10){
                ans = INT_MAX;
                break;
            }
            if  (neg && *str - '0' > -INT_MIN - ans * 10){
                ans = -INT_MIN;
                break;
            }
            ans = ans *10 + (*str - '0'); // 一开始忘记写
            str++;
        }
        ans = neg ?  -ans: ans;
        return ans;
} //12ms faster than 100%

/*c++ 方法
int myAtoi(string str) {
    long result = 0;
    int indicator = 1;
    for(int i = 0; i<str.size();)
    {
        i = str.find_first_not_of(' ');
        if(str[i] == '-' || str[i] == '+')
            indicator = (str[i++] == '-')? -1 : 1;
        while('0'<= str[i] && str[i] <= '9') 
        {
            result = result*10 + (str[i++]-'0');
            if(result*indicator >= INT_MAX) return INT_MAX;
            if(result*indicator <= INT_MIN) return INT_MIN;                
        }
        return result*indicator;
    }
}
*/