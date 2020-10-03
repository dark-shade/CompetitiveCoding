"""32 ms
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps_count = 0
        lower_count = 0
        
        for ch in word:
            if ord(ch) >= 65 and ord(ch) <= 90:
                caps_count += 1
                
            elif ord(ch) >= 97 and ord(ch) <= 122:
                lower_count += 1
            
        if caps_count == len(word) or lower_count == len(word) or (caps_count == 1 and ord(word[0]) >= 65 and ord(word[0]) <= 90):
            return True
        
        return False
"""
"""32 ms
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
"""