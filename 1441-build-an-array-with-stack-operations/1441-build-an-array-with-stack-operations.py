class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        idx = 0
        count = 0
        
        for i in range(1,n+1):
            if idx >= len(target):
                break
                
            elif target[idx] == i:
                
                while count > 0:
                    output.append("Pop")
                    count -= 1
                    
                output.append("Push")
                idx += 1
            
            else:
                output.append("Push")
                count += 1
            
            
        return output