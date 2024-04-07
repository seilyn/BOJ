n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):

        if i == 0 or i == n:
            dp[i][j] = dp[i][j-1] + maze[i][j]
        elif j == 0 or j == m:
            dp[i][j] = dp[i-1][j] + maze[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i][j]

print(dp[n-1][m-1])