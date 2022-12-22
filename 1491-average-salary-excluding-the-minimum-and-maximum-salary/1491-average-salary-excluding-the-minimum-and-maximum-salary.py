class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        total = sum(salary[1:len(salary)-1])
        
        
        return total/(len(salary) -2)
        
        