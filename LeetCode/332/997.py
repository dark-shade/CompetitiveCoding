"""812 ms 18.3 MB
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and N == 1:
            return 1
            
        people = set()
        people_trust = set()
        
        # of form {person : [trusted by]}
        trust_dict = {}
        
        for t in trust:
            people.add(t[0])
            people.add(t[1])
            people_trust.add(t[0])
            
            if t[1] not in trust_dict:
                trust_dict[t[1]] = []
                
            trust_dict[t[1]].append(t[0])
            
        for p in people:
            if p not in people_trust:
                if len(trust_dict[p]) == len(people) - 1:
                    return p
                
        return -1
"""