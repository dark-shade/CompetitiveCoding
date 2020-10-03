from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # form {word: {char: count}}
        counter = {}

        for word in A:
            if word not in counter:
                counter[word] = {}

            for ch in word:
                if ch not in counter[word]:
                    counter[word][ch] = 0
                counter[word][ch] += 1

        final_list = []

        for ch in counter[A[0]].keys():
            running_cnt = len(A[0])
            for word in counter.keys():
                if ch in counter[word]:
                    if running_cnt > counter[word][ch]:
                        running_cnt = counter[word][ch]
                else:
                    running_cnt = 0
                    break

            if running_cnt > 0:
                final_list.extend([ch] * running_cnt)

        return final_list
        