"""120 ms 13.7 MB
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        
        for letter in letters:
            if target < letter:
                return letter
"""