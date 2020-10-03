"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # of form {id : [imp, [subs]}
        imp_map = {}
        
        for emp in employees:
            imp_map[emp.id] = [emp.importance, emp.subordinates]
            
        total_imp = self.getAllSubs(imp_map, id)
        
        return total_imp
                
    def getAllSubs(self, imp_map, id):
        imp = imp_map[id][0]
        
        for emp in imp_map[id][1]:
            imp += self.getAllSubs(imp_map, emp)
            
        return imp
            
            
        
            
            