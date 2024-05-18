import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    next = arr[x]

    if not visited[next]:
        dfs(next)
    return

case = int(input())


for _ in range(case):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    cycle = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cycle += 1

    print(cycle)



