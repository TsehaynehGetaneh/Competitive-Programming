import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

even = 0
odd = 0
for i in range(len(arr)):
    if arr[i]%2 == 0:
        even += 1
    else:
        odd += 1

if even > 0 and odd > 0:
    arr.sort()

# print elements
print(*arr)
