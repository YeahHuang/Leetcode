class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        #一开始的时候写的是s.split(' ')反而不ok 学到了吖
    
    #C++ Sol
    '''
    void reverseWords(string &s) {
    istringstream is(s);
    string tmp;
    is >> s;
    while(is >> tmp) s = tmp + " " + s;
    if(s[0] == ' ') s = "";
}
'''