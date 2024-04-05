n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(n)] for _ in range(n)]

d[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            d[i][j] = d[i-1][j] + arr[i][j]
        elif j == len(arr[i])-1:
            d[i][j] = d[i-1][j-1] + arr[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + arr[i][j]

print(max(d[n-1]))
