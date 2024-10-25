class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        d = Counter(folder) # o(n)

        for sub_folder in folder: # o(n)
            sub_f = sub_folder.strip("/").split("/") # 0(m)
            sub = "" # o(m-1)
            for i in range(len(sub_f)-1): # o(m-1)
                sub += "/" + sub_f[i]
                
                if sub in d: # o(1)
                    del d[sub_folder] # o(1)
                    break

        return list(d.keys())

# time complexity: o(n*m)
