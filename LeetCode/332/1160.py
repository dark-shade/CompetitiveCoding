from typing import List
import collections

"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = collections.Counter(chars)
        
        total_len = 0
                
        for w in words:
            word_counter = collections.Counter(w)
            
            if word_counter == (chars_counter & word_counter):
                total_len += len(w)
                
        return total_len
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for w in words:
            included = True
            charsList = [c for c in chars]
            for c in w:
                if c in charsList:
                    charsList.remove(c)
                else:
                    included = False
                    break
            if included: counter = counter+len(w)
        return counter