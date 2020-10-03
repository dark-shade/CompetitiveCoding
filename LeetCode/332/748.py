"""152 ms
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_coll = collections.Counter(licensePlate.lower())
        smallest_word = ""
        
        for w in words:
            completes = True
            diff = lp_coll - collections.Counter(w)
            
            for ch in diff:
                if ord(ch) >= 97 and ord(ch) <= 122:
                    completes=False
                    break
                    
            if completes:
                if len(smallest_word) > 0:
                    if len(smallest_word) > len(w):
                        smallest_word = w
                    elif len(smallest_word) == len(w):
                        if words.index(smallest_word) > words.index(w):
                            smallest_word = w
                else:
                    smallest_word = w
                    
        return smallest_word
"""
"""160 ms
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_coll = collections.Counter(licensePlate.lower())
        smallest_word = ""
        small_ind = 0
        
        for i, w in enumerate(words):
            completes = True
            diff = lp_coll - collections.Counter(w)
            
            for ch in diff:
                if ord(ch) >= 97 and ord(ch) <= 122:
                    completes=False
                    break
                    
            if completes:
                if len(smallest_word) > 0:
                    if len(smallest_word) > len(w):
                        smallest_word = w
                        small_ind = i
                    elif len(smallest_word) == len(w):
                        if small_ind > i:
                            smallest_word = w
                            small_ind = i
                else:
                    smallest_word = w
                    small_ind = i
                    
        return smallest_word
"""
"""136 ms
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = ""
        for ch in licensePlate.lower():
            if ord(ch) >= 97 and ord(ch) <= 122:
                lp += ch
                
        lp_coll = collections.Counter(lp)
        smallest_word = ""
        small_ind = 0
        
        for i, w in enumerate(words):
            completes = True
            diff = lp_coll - collections.Counter(w)
            
            if len(diff) > 0:
                continue        
            
            if len(smallest_word) > 0:
                if len(smallest_word) > len(w):
                    smallest_word = w
                    small_ind = i
                elif len(smallest_word) == len(w):
                    if small_ind > i:
                        smallest_word = w
                        small_ind = i
            else:
                smallest_word = w
                small_ind = i
                    
        return smallest_word   
"""
"""112 ms
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = ""
        for ch in licensePlate.lower():
            if ord(ch) >= 97 and ord(ch) <= 122:
                lp += ch
                
        lp_coll = collections.Counter(lp)
        smallest_word = ""
        small_ind = 0
        
        for i, w in enumerate(words):
            if len(w) < len(lp):
                continue
                
            completes = True
            diff = lp_coll - collections.Counter(w)
            
            if len(diff) > 0:
                continue        
            
            if len(smallest_word) > 0:
                if len(smallest_word) > len(w):
                    smallest_word = w
                    small_ind = i
                elif len(smallest_word) == len(w):
                    if small_ind > i:
                        smallest_word = w
                        small_ind = i
            else:
                smallest_word = w
                small_ind = i
                    
        return smallest_word            
"""