from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # form {student id: [scores]}
        scores = {}
        final = []

        for student_id, score in items:
            if student_id not in scores:
                scores[student_id] = []
            
            scores[student_id].append(score)

        for student_id in scores.keys():
            scores[student_id].sort(reverse=True)
            final.append([student_id, int(sum(scores[student_id][:5])/5)])
        
        return final
