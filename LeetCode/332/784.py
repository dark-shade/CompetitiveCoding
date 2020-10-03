from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        per = self.getPermutations([S], 0)
        per_set = set(per)
        return list(per_set)

    def getPermutations(self, per, ind):
        print(per)
        
        for S in per:
            for i in range(ind, len(S)):
                recc = False
                
                if (ord(S[i]) >= 65 and ord(S[i]) <= 90) or (ord(S[i]) >= 97 and ord(S[i]) <= 122):
                    low = S[:i] + S[i].lower()
                    up = S[:i] + S[i].upper()

                    if i < len(S) - 1:
                        low += S[i+1:]
                        up += S[i+1:]

                    if low not in per:
                        per.append(low)
                        recc = True
                    if up not in per:
                        per.append(up)
                        recc = True
        
                    if recc:
                        per = self.getPermutations(per, i+1)
                    break

        return per