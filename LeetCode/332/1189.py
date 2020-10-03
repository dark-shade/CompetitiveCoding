class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        
        num = -1
        
        for ch in "balon":
            if ch not in cnt:
                return 0
            
            if ch in "ban":
                if num == -1 or cnt[ch] < num:
                    num = cnt[ch]
            else:
                if num == -1 or int(cnt[ch]/2) < num:
                    num = int(cnt[ch]/2)
                
        return num 
        
            
        