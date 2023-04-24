class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        visited = set()
        def dfs(parent):
            nonlocal ans,visited
            visited.add(parent)
            
            if parent not in self.deaths:
                ans.append(parent)
            for child in self.graph[parent]:
                dfs(child)
        
        dfs(self.kingName)
        
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()