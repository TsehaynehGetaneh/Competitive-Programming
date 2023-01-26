import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    # store subsequence elements with max sum
    sub_arr = [arr[0]]

    for i in range(1,len(arr)):
        if arr[i] > 0 and sub_arr[-1] > 0 or arr[i] < 0 and sub_arr[-1] < 0:
            if arr[i] > sub_arr[-1]:
                sub_arr.pop()
                sub_arr.append(arr[i])

        else:
            sub_arr.append(arr[i])

    print(sum(sub_arr))

        



