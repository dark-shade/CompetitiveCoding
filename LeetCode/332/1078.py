class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        thirds = []
        pos = False
        add_next = False
        
        for word in text.split():
            if add_next:
                thirds.append(word)
                add_next = False
            
            if word == first:
                pos = True
                continue
                
            if pos:
                if word == second:
                    add_next = True
                pos = False
                
        return thirds               