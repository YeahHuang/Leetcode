class Solution:
    #36ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]"," ", paragraph.lower())
        counter = collections.Counter(paragraph.split())
        #把⬆️两行换成⬇️ 36ms -> 32ms
        #counter = collections.Counter(re.split('\W+',paragraph.lower()))
        banned = set(banned)
        for s in sorted(counter, key=counter.get, reverse=True):
            if s not in banned:
                return s

    #36ms
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

'''
关于re 正则表达式 https://docs.python.org/2/library/re.html#regular-expression-objects
re.split('\w+', 'Words, words, words.')
['Words', 'words', 'words', '']

re.sub(pattern, repl, string, count=0, flags=0)
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'
'''