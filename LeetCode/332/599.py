"""256 ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_cnt = -1
        min_choice = []
        
        #of form {"place": sum of indexes}
        cnt = {}
        
        common = set(list1) & set(list2)
        
        for i in range(len(list1)):
            if list1[i] in common:
                cnt[list1[i]] = i
            
        for j in range(len(list2)):
            if list2[j] in common:
                cnt[list2[j]] += j
                
        for k in cnt:
            if min_cnt == -1:
                min_cnt = cnt[k]
                min_choice.append(k)
                continue
                
            if cnt[k] < min_cnt:
                min_cnt = cnt[k]
                min_choice = [k]
                
            elif cnt[k] == min_cnt:
                min_choice.append(k)
                
        return min_choice
"""
"""216 ms
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_cnt = -1
        min_choice = []
        
        #of form {"place": [sum of indexes, common: bool]}
        cnt = {}
        
        for i in range(len(list1)):
            cnt[list1[i]] = [i, False]
            
        for j in range(len(list2)):
            if list2[j] in cnt:
                cnt[list2[j]][0] += j
                cnt[list2[j]][1] = True
                
        for k in cnt:
            if not cnt[k][1]:
                continue
            
            if min_cnt == -1:
                min_cnt = cnt[k]
                min_choice.append(k)
                continue
                
            if cnt[k] < min_cnt:
                min_cnt = cnt[k]
                min_choice = [k]
                
            elif cnt[k] == min_cnt:
                min_choice.append(k)
                
        return min_choice
"""