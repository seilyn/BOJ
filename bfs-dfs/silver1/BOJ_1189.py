
def dfs(x, y, depth):

    global count
    # 방문한 곳은 T로 표시 한다.
    graph[x][y] = 'T'

    if depth == k and x == 0 and y == c - 1:
        count += 1


    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 'T':
            graph[nx][ny] = 'T'
            dfs(nx, ny, depth + 1)
            graph[nx][ny] = '.'

r,c,k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


dfs(r-1, 0, 1)
print(count)
