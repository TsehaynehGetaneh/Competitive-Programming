class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,0,-1):
            if arr[i-1] > arr[i]:
                # print(i-1)
                for j in range(len(arr)-1,i-1,-1):
                    if arr[j] < arr[i-1] and arr[j] != arr[j-1]:
                        arr[i-1],arr[j] = arr[j],arr[i-1]
                        return arr
        else:
            return arr
        