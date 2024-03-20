import sys
from collections import deque


n = int(sys.stdin.readline())
start, end = map(int,sys.stdin.readline().split())
case = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(case):

    x, y = map(int, sys.stdin.readline().split())

    graph[x].append(y)
    graph[y].append(x)

queue = deque([start])
visited[start] = 1
flag = False

while queue:

    current = queue.popleft()

    if current == end:
        break

    for next in graph[current]:
        if visited[next] == 0:

            visited[next] = visited[current] + 1
            queue.append(next)

print(visited[end]-1)