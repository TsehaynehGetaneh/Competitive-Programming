class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        d = Counter(folder)

        for sub_folder in folder:
            sub_f = sub_folder.strip("/").split("/")
            sub = ""
            for i in range(len(sub_f)-1):
                sub += "/" + sub_f[i]
                
                if sub in d:
                    del d[sub_folder]
                    break

        return list(d.keys())
