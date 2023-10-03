class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = [None,None]
        L = len(bin(max(nums))) - 2 # binary length of max num in nums
        max_xor = 0
        
        for Num in nums:
            num = [Num>>i & 1 for i in range(L-1,-1,-1)] 
            ptr1 = trie 
            ptr2 = trie
            xor = 0
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
                        xor |= 1 # add 1 to xor if toggle bit exists
                    else:
                        ptr2 = ptr2[bit]
                        
                else:
                    if ptr1[bit]:
                        ptr1 = ptr1[bit]
                    else:
                        ptr1[bit] = [None,None]
                        ptr1 = ptr1[bit]
                        
                    if ptr2[toggle]:
                        ptr2 = ptr2[toggle]
                        xor |= 1 # add 1 to xor if toggle bit exists
                    else:
                        ptr2 = ptr2[bit]
                
                xor <<= 1 # shift xor to left by one bit
                
            xor >>= 1 # remove the extra zero bit at the end
            max_xor = max(max_xor,xor) 
            
        return max_xor
