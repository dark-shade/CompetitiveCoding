class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # temp ds to store grp while being created
        groups = {}
        grps = []
        
        for i, n in enumerate(groupSizes):
            if n not in groups:
                groups[n] = []
            
            groups[n].append(i)
            
            if len(groups[n]) == n:
                grps.append(groups[n])
                groups[n] = []
                
        return grps
                