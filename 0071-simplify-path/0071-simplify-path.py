class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        
        for path_ in path:
            if stack and path_ == "..":
                stack.pop()
                
            elif path_ != "." and path_ != "" and path_ != "..":
                stack.append(path_)
                
        ans = "/" + "/".join(stack)
        
        return ans
            
        