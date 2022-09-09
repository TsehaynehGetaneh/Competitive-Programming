def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)):
        swapped =False
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp =a[j]
                a[j]= a[j+1]
                a[j+1]=temp
                swapped = True
                numSwaps +=1
        if not swapped:
            break
    def result():
        print(f"Array is sorted in {numSwaps} swaps.")
        print(f"First Element: {a[0]}")
        print(f"Last Element: {a[len(a)-1]}")
    return  result()