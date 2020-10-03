from typing import List
import collections

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # of form {string : [even_ctr, odd_ctr]}
        st_dict = {}
        
        for s in A:
            st_dict[s] = self.getCounts(s)

        max_cnt = 0

        for i in range(len(A)):
            cnt = 1
            for j in range(i+1, len(A)):
                if st_dict[A[i]][0] == st_dict[A[j]][0] and st_dict[A[i]][1] == st_dict[A[j]][1]:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt

        return max_cnt

    def getCounts(self, st):
        even_loc = []
        odd_loc = []

        for i, s in enumerate(st):
            if i % 2 == 0:
                even_loc.append(s)
            else:
                odd_loc.append(s)

        even_ctr = collections.Counter(even_loc)
        odd_ctr = collections.Counter(odd_loc)

        return [even_ctr, odd_ctr]
