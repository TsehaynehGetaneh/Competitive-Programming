import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n,m = list(map(int,input().split()))
    
    grid = []
    for i in range(n):
        row = list(map(int,input().split()))
        grid.append(row)

    diagonal1 = {}
    diagonal2 = {}
    for i in range(n):
        for j in range(m):
            idx_sum = i +j
            idx_diff = j -i
            if idx_sum in diagonal1:
                diagonal1[idx_sum] += grid[i][j]
            else:
                diagonal1[idx_sum] = grid[i][j]

            if idx_diff in diagonal2:
                diagonal2[idx_diff] += grid[i][j]
            else:
                diagonal2[idx_diff] = grid[i][j]

    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum,diagonal1[i+j] + diagonal2[j-i] - grid[i][j])

    
    print(max_sum)


            

    
