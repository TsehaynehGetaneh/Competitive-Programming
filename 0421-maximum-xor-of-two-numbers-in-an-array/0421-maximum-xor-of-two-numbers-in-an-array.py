class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = [None,None]
        L = len(bin(max(nums))) - 2 # binary length of max num in nums
        max_xor = 0
        
        for Num in nums:
            num = [Num>>i & 1 for i in range(L-1,-1,-1)] 
            ptr1 = trie 
            ptr2 = trie
            xor = []
            for bit in num:
                toggle = 1 - bit 
                if bit:
                    if ptr1[bit]:
                        ptr1 = ptr1[bit]
                    else:
                        ptr1[bit] = [None,None]
                        ptr1 = ptr1[bit]
                        
                    if ptr2[toggle]:
                        ptr2 = ptr2[toggle]
                        xor.append("1")
                    else:
                        ptr2 = ptr2[bit]
                        xor.append("0")
                        
                else:
                    if ptr1[bit]:
                        ptr1 = ptr1[bit]
                    else:
                        ptr1[bit] = [None,None]
                        ptr1 = ptr1[bit]
                        
                    if ptr2[toggle]:
                        ptr2 = ptr2[toggle]
                        xor.append("1")
                    else:
                        ptr2 = ptr2[bit]
                        xor.append("0")
                 
            xor = int("".join(xor),2)
            
            max_xor = max(max_xor,xor) 
            
        return max_xor
    
    
    
    
