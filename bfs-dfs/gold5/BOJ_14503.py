from collections import deque

n,m = map(int,input().split())
r,c,d = map(int,input().split())

area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0
#     북  동  남  서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def print_area():
    for row in range(n):
        for col in range(m):
            if visited[row][col]:
                print('*', end=' ')
            else:
                print(area[row][col], end=' ')
        print()
    print()
def bfs(x, y, direction):
    queue = deque()
    global count

    visited[x][y] = True

    queue.append([x, y])
    count += 1
    while queue:

        x, y = queue.popleft()
        flag = False

        # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
        # 반시계 방향으로 회전 시
        # 0->3, 3->2, 2->1, 1->0
        for i in range(4):
            direction = (direction+3) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
                count += 1
                flag = True
                break
                # print_area()
                # break
        if not flag:
            if area[x-dx[direction]][y-dy[direction]] != 1:
                queue.append([x-dx[direction], y-dy[direction]])
            else:
                print(count)
                break

bfs(r,c,d)



