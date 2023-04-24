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
        total_importance = 0
        graph = {} # contains each employee class
        for employee in employees:
            graph[employee.id] = employee
        
        # DFS
        def dfs(employee):
            nonlocal total_importance 
            
            
            total_importance += employee.importance
            for child in employee.subordinates:
                dfs(graph[child])
        
        # call dfs
        dfs(graph[id])
                
        return total_importance