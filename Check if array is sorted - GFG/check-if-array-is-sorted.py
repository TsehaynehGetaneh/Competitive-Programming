#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        if len(arr) == 1:
            return 1
        
        else:
            i = 0
            j = 1
            while i<j and j < len(arr):
                if arr[j] < arr[i]:
                    return 0
                    
                i += 1
                j += 1
                    
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends