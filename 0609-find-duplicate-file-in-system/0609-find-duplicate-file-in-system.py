class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        output = []
        
        for path in paths:
            path = path.split()
            for i in range(1,len(path)):
                p = path[i].split("(")
                p1 = p[0]
                content = p[1][:-1]
                
                new_path = path[0] + "/" + p1
                
                dic[content].append(new_path)
            
        
        for key,val in dic.items():
            if len(val) > 1:
                output.append(val)
            
        return output