from typing import List
import math

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        total_cnt = 0
        line_cnt = 1

        for ch in S:
            word_cnt = widths[ord(ch) - 97]
            
            if total_cnt + word_cnt > 100:
                line_cnt += 1
                total_cnt = word_cnt
            else:
                total_cnt += word_cnt

        return [line_cnt, total_cnt]
