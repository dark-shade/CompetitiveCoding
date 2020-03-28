class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # {char: count}
        char_count = {}
        num_odd = 0

        for ch in s:
            if ch not in char_count:
                char_count[ch] = 0
            char_count[ch] += 1
        
        for ch in char_count.keys():
            if char_count[ch] % 2 != 0:
                num_odd += 1
                if num_odd > 1:
                    return False
                
        return True

obj = Solution()
palin = obj.canPermutePalindrome("")            
print(palin)
