class Solution:
    def validate_IPv4(self,queryIP):
        if len(queryIP) > 15:
            return False
        
        arr = queryIP.split(".")
        if len(arr) != 4:
            return False
        
        for x in arr:
            if not x.isdigit():
                return False
            
            if x[0] == "0" and len(x) != 1:
                return False
            
            if int(x) < 0 or int(x) > 255:
                return False
            
        return True
            
    def validate_IPv6(self,queryIP):
        if len(queryIP) > 39:
            return False
        
        arr = queryIP.split(":")
        if len(arr) != 8:
            return False
        
        pattern = "^[a-fA-F0-9]+$"
        for x in arr:
            if not bool(re.fullmatch(pattern,x)):
                return False
            
            if len(x) < 1 or len(x) > 4:
                return False
            
        return True
              
    def validIPAddress(self, queryIP: str) -> str:
        is_IPv4 = self.validate_IPv4(queryIP)
        if is_IPv4:
            return "IPv4"
        
        is_IPv6 = self.validate_IPv6(queryIP)
        if is_IPv6:
            return "IPv6"
        
        return "Neither"
        
        
        
        
        
        
        
        
        
        
        
        