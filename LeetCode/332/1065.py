"""40 ms
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # of form {length: [words]}
        word_map = {}
        
        pairs = []
                
        for w in words:
            if len(w) not in word_map:
                word_map[len(w)] = []
            word_map[len(w)].append(w)
        
        for s in word_map:
            if s <= len(text):
                start_ptr = 0
                for i in range(s, len(text)+1):
                    if text[start_ptr : i] in word_map[s]:
                        pairs.append([start_ptr,i-1])
                        
                    start_ptr += 1
        
        pairs.sort()
        
        return pairs
"""
""" 28 ms
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # of form {length: { "first char" : [words]}
        word_map = {}
        
        pairs = []
                
        for w in words:
            if len(w) not in word_map:
                word_map[len(w)] = {}
            if w[0] not in word_map[len(w)]:
                word_map[len(w)][w[0]] = []
            word_map[len(w)][w[0]].append(w)
        
        for s in word_map:
            if s <= len(text):
                start_ptr = 0
                for i in range(s, len(text)+1):
                    if text[start_ptr] in word_map[s]:
                        if text[start_ptr : i] in word_map[s][text[start_ptr]]:
                            pairs.append([start_ptr,i-1])
                        
                    start_ptr += 1
        
        pairs.sort()
        
        return pairs
"""