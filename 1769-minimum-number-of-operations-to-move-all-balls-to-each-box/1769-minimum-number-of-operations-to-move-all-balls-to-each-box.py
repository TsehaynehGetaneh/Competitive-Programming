class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        indices_one = []
        
        for i in range(len(boxes)):
            if boxes[i] == "1":
                indices_one.append(i)
               
        for i in range(len(boxes)):
            count = 0
            for j in range(len(indices_one)):
                val = abs(indices_one[j]-i)
                count += val
            
            output.append(count)
            
        return output
                
            
        
        
        