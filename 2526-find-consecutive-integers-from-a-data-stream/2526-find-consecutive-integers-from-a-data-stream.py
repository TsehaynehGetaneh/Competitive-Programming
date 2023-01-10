class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.values = []
        self.notValues = []
        self.idx = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.values.append(self.idx)
    
        if num != self.value:
            self.notValues.append(self.idx)
            
        self.idx += 1
        
        if len(self.values) < self.k:
            return False
        
        if len(self.values) >= self.k:
            if len(self.values) >= self.k and len(self.notValues) == 0:
                return True
            
            elif len(self.values) >= self.k and len(self.notValues) >0:
                if self.values[-1]- self.notValues[-1] >= self.k:
                    return True
                else:
                    return False
            
            
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)