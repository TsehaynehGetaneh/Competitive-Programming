class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        for num in asteroids:
            ans.append(num)
            
            while len(ans) > 1 and (ans[-2] > 0 and ans[-1] < 0):
                if abs(ans[-1]) < abs(ans[-2]):
                    ans.pop()
                elif abs(ans[-2]) < abs(ans[-1]):
                    num = ans.pop()
                    ans.pop()
                    ans.append(num)
                    
                elif abs(ans[-1]) == abs(ans[-2]):
                    ans.pop()
                    ans.pop()
                    
                    
        return ans
                    