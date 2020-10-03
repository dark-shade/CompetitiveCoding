class Solution:
    def toGoatLatin(self, S: str) -> str:
        final_str = ""
        
        for i, w in enumerate(S.split()):
            if str(w[0]) in "aeiouAEIOU":
                final_str += w + "ma"
            else:
                if len(w) > 1:
                    final_str += str(w[1:])
                final_str += str(w[0]) + "ma"
                
            final_str += "a" * (i + 1) + " "
            
        return final_str.strip()
            
            