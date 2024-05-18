import sys

def dfs(x,val, depth=1):
    global cost
    global first

    if depth == n:
        for nx, c in graph[x]:
            if nx == first:
                cost = min(cost, val+c)
        return

    if visited[x]:
        return

    visited[x] = True

    for nx, c in graph[x]:
        if not visited[nx]:
            dfs(nx,val+c,depth+1)
            visited[nx] = False


input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
cost = float('inf')
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if i == j or temp[j] == 0:
            continue
        graph[i].append((j, temp[j]))


for i in range(n):
    visited = [False] * n
    first = i
    dfs(i,0)

print(cost)

