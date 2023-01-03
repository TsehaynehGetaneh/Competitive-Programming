class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        result = []
        
        for domain in cpdomains:
            domain = domain.split()
            visited_time = int(domain[0])
            main_domain = domain[1]
            
            sub_domains = main_domain.split(".")
            sub_domain1 = '.'.join(sub_domains[1:])
            sub_domain2 = '.'.join(sub_domains[2:])
            
            arr = [main_domain, sub_domain1, sub_domain2]
            print(arr)
            for i in range(len(arr)):
                if arr[i] != "":
                    
                    if arr[i] in dic:
                        dic[arr[i]] += visited_time
                    else:
                        dic[arr[i]] = visited_time
                        
        for key,val in dic.items():
            result.append(f"{val} {key}")
            
        return result
                    
            
                
            
            
            
            
            
        