def insertionSort1(n, arr):
    # Write your code here
    rightmost = arr[n-1]
    for i in range(n-1, -1, -1):
        if i == 0 and rightmost < arr[i]:
            arr[i] = rightmost
            for i in range(n):
                print(arr[i], end= " ")
            print()
            
        elif rightmost < arr[i-1]:
            arr[i] = arr[i-1]
            for i in range(n):
                print(arr[i], end= " ")
            print()
            
        else:
            arr[i] = rightmost
            for i in range(n):
                print(arr[i], end = " ")
            print()
            break
