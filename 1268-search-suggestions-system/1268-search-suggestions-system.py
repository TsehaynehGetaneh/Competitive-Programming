class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        
        for (i,char) in enumerate(searchWord):
            count = 0
            res = []
            for product in products:
                if product[:i+1] == searchWord[:i+1]:
                    res.append(product)
                    count += 1
                    
                if count == 3:
                    break
                    
            ans.append(res)
            
        return ans
                
            
        