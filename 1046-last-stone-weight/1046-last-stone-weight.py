class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n//2 -1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # Build heap (rearrange array)
        self.buildHeap(arr, n)

        # One by one extract an element from heap
        for i in range(n - 1, 0, -1):
            # Move current root to end
            arr[i], arr[0] = arr[0], arr[i]

            # call max heapify on the reduced heap
            self.heapify(arr, i, 0)
            
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            self.HeapSort(stones,len(stones))
            print(stones)
            if stones[-2] == stones[-1]:
                stones.pop()
                stones.pop()
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
                
        
        if stones:
            return stones[0]
        else:
            return 0