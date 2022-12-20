# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    
from collections import Counter
c = Counter(arr)
print(len(c))
for key in c:
    print(c[key], end = ' ')
    
