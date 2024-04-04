import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
length = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 1번 부터 검색
queue = deque([1])
visited[1] = True

while queue:
    current = queue.popleft()

    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            length[next] = length[current] + 1
            queue.append(next)

# 최대값 지정
temp = max(length)
result = []

for i,v in enumerate(length):
    if v == temp:
        result.append(i)
        result.append(temp)
        result.append(length.count(temp))
        break

print(*result, sep=' ')





