class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr_alt = 0
        for i in range(len(gain)):
            curr_alt += gain[i]
            ans = max(ans,curr_alt)
            
        return ans

        