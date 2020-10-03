"""64 ms
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # of form {ch : index}
        od = {}
        
        for i in range(len(order)):
            od[order[i]] = i
        
        #check two words rather than one char for all words
        for i in range(1, len(words)):
            if not self.lexOrdered(words[i-1], words[i], od):
                return False
            
        return True
            
            
    def lexOrdered(self, word1, word2, od):
        for i in range(len(word1)):
            if i >= len(word2) or od[word1[i]] > od[word2[i]]:
                return False
            
            if od[word1[i]] < od[word2[i]]:
                return True
            
        return True
"""