class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # form {char in s : char in t}
        mapping = {}
        already_mapped = set()
        
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in already_mapped:
                    mapping[s[i]] = t[i]
                    already_mapped.add(t[i])
                else:
                    return False
            else:
                if mapping[s[i]] != t[i]:
                    return False
                
        return True
            
        