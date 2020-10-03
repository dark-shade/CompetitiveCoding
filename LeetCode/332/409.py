class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        
        length = 0
        added_one = False
        odd_present = False
        
        for ch in cnt:
            if cnt[ch] % 2 == 0:
                length += cnt[ch]
            else:
                odd_present = True
                length += cnt[ch] - 1
                        
            if cnt[ch] == 1 and not added_one:
                length += 1
                added_one = True
                
        if not added_one and odd_present:
            length += 1
                
        return length