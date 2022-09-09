class Solution: 
    def select(self, arr, i):
        for i in range(len(arr)-1):
            current_index = i
            for j in range(i+1, len(arr)):
                if arr[current_index] > arr[j]:
                    current_index = j
        return current_index
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            current_index = i
            for j in range(i+1, len(arr)):
                if arr[current_index] > arr[j]:
                    current_index = j
            arr[current_index],arr[i] = arr[i], arr[current_index]
        return arr