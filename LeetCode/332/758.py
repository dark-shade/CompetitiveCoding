"""140 ms 14 MB
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        if len(words) == 0 or len(S) == 0:
            return S
        
        bold = set()
        
        for keyword in words:
            for i in range(len(S) - len(keyword) + 1):
                if S[i : i+len(keyword)] == keyword:
                    for j in range(i, i + len(keyword)):
                        bold.add(j)
            
        new_S = ""
        bold_flag = False
        
        print(bold)
        
        for i, ch in enumerate(S):
            if i in bold and not bold_flag:
                bold_flag = True
                new_S += "<b>" + ch
            elif i not in bold and bold_flag:
                bold_flag = False
                new_S += "</b>" + ch
            else:
                new_S += ch
        
        if len(S) - 1 in bold:
            new_S += "</b>"
                
        return new_S
"""
