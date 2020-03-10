class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = "aeiou"
        final = ""

        for ch in S:
            if ch not in vowels:
                final += ch
        
        return final

obj = Solution()
f = obj.removeVowels("aeioud")
print(f)
