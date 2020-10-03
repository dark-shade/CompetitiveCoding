"""324 ms
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_f = []
        
        for w in words:
            words_f.append(self.minFreq(w))
            
        words_f.sort(reverse=True)
        f_cnts = []
        
        print(words_f)
        
        for q in queries:
            qf = self.minFreq(q)
            print(qf)    
            curr = 0
            
            for wf in words_f:
                if qf < wf:
                    curr += 1
                else:
                    break
                    
            f_cnts.append(curr)
            
        return f_cnts
            
            
    def minFreq(self, word: str) -> int:
        min_word = word[0]
        cnt = 0
        
        for ch in word:
            if ch < min_word:
                min_word = ch
                cnt = 1
                
            elif ch == min_word:
                cnt += 1
                
        return cnt
"""

"""376 ms
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_f = []
        
        for w in words:
            words_f.append(self.minFreq(w))
            
        words_f.sort(reverse=True)
        f_cnts = []
        
        print(words_f)
        
        for q in queries:
            qf = self.minFreq(q)
            print(qf)    
            curr = 0
            
            for wf in words_f:
                if qf < wf:
                    curr += 1
                else:
                    break
                    
            f_cnts.append(curr)
            
        return f_cnts
            
            
    def minFreq(self, word: str) -> int:
        ctr = collections.Counter(word)
        
        return ctr[min(list(ctr.keys()))]
"""
