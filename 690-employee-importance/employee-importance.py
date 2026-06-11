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
        employee_map = {employee.id:employee for employee in employees}
        def dfs(employee_id):
            answer = employee_map[employee_id].importance
            for subordinate_id in employee_map[employee_id].subordinates:
                answer += dfs(subordinate_id)
            return answer 
        return dfs(id)
    


        
