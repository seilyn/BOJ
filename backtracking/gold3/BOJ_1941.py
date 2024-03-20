from collections import deque

def bfs(x, y):
    queue = deque()



classes = [list(map(str, input())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(5):
    for j in range(5):
        bfs(i,j)