class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N_before = [0] * (len(customers)+1)
        Y_after = [0] * (len(customers)+1)
        penality = [0] * (len(customers)+1)
        
        for i in range(len(customers)):
            if i == 0 and customers[i] == "N":
                N_before[i] += 1
            elif customers[i] == "N":
                N_before[i] += (N_before[i-1]+1)
            else:
                N_before[i] = N_before[i-1]
                
        N_before[-1] = N_before[-2]
                
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == "Y":
                Y_after[i] += (Y_after[i+1]+1)
            else:
                Y_after[i] = Y_after[i+1]
                
        for i in range(len(penality)-1,-1,-1):
            if i == 0:
                penality[i] = Y_after[i]
            else:
                penality[i] = N_before[i-1] + Y_after[i]
            
        
            
        res = [(0,penality[0])]
        for i in range(len(penality)):
            if penality[i] < res[0][1]:
                res = [(i,penality[i])]
                
        return res[0][0]
                
                
        