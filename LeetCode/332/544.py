"""52 ms
class Solution:
    def findContestMatch(self, n: int) -> str:
        if n == 2:
            return "(1,2)"
        
        front = 1
        end = n
        
        fixtures = []
        
        while front < end:
            fixtures.append("(" + str(front) + "," + str(end) + ")")
            front += 1
            end -= 1
        
        while len(fixtures) != 2:
            front = 0
            end = len(fixtures) - 1
            temp = []
            
            while front < end:
                temp.append("(" + fixtures[front] + "," + fixtures[end] + ")")
                front += 1
                end -= 1
            fixtures = temp
            
        return "(" + ",".join(fixtures) + ")"
"""    
            
        
        
            