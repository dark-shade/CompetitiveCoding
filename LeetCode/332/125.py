"""48 ms 14.5 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        new_s = ""
        
        for ch in s.lower():
            ch_val = ord(ch)
            if (ch_val >= 97 and ch_val <= 122) or (ch_val >= 48 and ch_val <= 57):
                new_s += ch
            
        if new_s == new_s[::-1]:
            return True
        
        return False
"""
"""48 ms 14.4 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        s = s.lower()
        front = 0
        end = len(s) - 1
        
        while front <= end:
            front_val = ord(s[front])
            end_val = ord(s[end])
            
            if not ((front_val >= 97 and front_val <= 122) or (front_val >= 48 and front_val <= 57)):
                front += 1
                continue
            
            if not ((end_val >= 97 and end_val <= 122) or (end_val >= 48 and end_val <= 57)):
                end -= 1
                continue
                
            if front_val != end_val:
                return False
            
            front += 1
            end -= 1
        
        return True
"""