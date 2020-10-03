class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        for i in range(len(num)):
            if num[i] == num[len(num) -1 - i] and num[i] not in "018":
                return False
            
            if num[i] != num[len(num) -1 - i] and (num[i] not in "69" or num[len(num) -1 - i] not in "69"):
                return False
            
        return True