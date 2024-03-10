from collections import deque


def bfs(x, y, z):

    queue = deque()
    queue.append([x, y, z])
    visited[x][y][z] = True

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if buildings[nx][ny][nz] == 'E':
                    print('Escaped in {0} minute(s).'.format(visited[x][y][z]))
                    return
                if buildings[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append([nx, ny, nz])

    print('Trapped!')

while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    buildings = [[[] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        buildings[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0 ,0, 0, 0, -1, 1]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if buildings[i][j][k] == 'S':
                    bfs(i,j,k)

