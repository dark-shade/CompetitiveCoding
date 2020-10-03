"""32 ms 14.1 MB
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        itr = 0 
        
        while itr + len(needle) <= len(haystack):
            if haystack[itr:itr+len(needle)] == needle:
                return itr
            itr += 1
            
        return -1
"""
"""36 ms 14 MB
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        if len(haystack) == 0 or len(needle) > len(haystack):
            return -1
        
        #using simple hash function, a...z = 1...26, additive hash
        itr = 0 
        needle_hash = 0
        window_hash = 0
                
        while itr < len(needle):
            needle_hash += ord(needle[itr]) - 97 + 1
            window_hash += ord(haystack[itr]) - 97 + 1
            itr += 1
            
        while itr < len(haystack):
            if needle_hash == window_hash and needle == haystack[itr-len(needle):itr]:
                return itr - len(needle)
            
            window_hash -= ord(haystack[itr - len(needle)]) - 97 + 1
            window_hash += ord(haystack[itr]) - 97 + 1
            itr += 1
            
        if needle_hash == window_hash and needle == haystack[itr-len(needle):itr]:
            return itr - len(needle)
            
        return -1
"""