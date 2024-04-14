# 내일다시풀어볼것

r, c = map(int, input().split())
board = [list(map(str, input())) for _ in range(r)]
direction = list(map(int, input()))

# 움직일 거리
dx = [-9, 1, 1, 1,  0, 0, 0, -1, -1, -1]
dy = [-9, -1, 0, 1, -1, 0, 1, -1,  0,  1]

loc_jongsu = [(x,y) for x in range(r) for y in range(c) if board[x][y] == 'I'][0]
loc_arduino = [(x,y) for x in range(r) for y in range(c) if board[x][y] == 'R']

def move_arduino():
    j_x, j_y = loc_jongsu

    for x, y in loc_arduino:
        min_dist = 99999999
        min_loc = (0,0)
        board[x][y] = '.'

        for d in range(1, 10):

            if d == 5:
                continue

            nx = x + dx[d]
            ny = y + dy[d]



            if 0 < nx <= r and 0 < ny <= c:


                dist = abs(nx-j_x) + abs(ny-j_y)

                if min_dist > dist:
                    min_dist = dist
                    min_loc = (nx, ny)
                    board[nx][ny] = 'R'


def move(direction):
    global loc_jongsu


    for d in direction:
        x, y = loc_jongsu
        nx = x + dx[d]
        ny = y + dy[d]

        loc_jongsu = (nx, ny)
        board[x][y] = '.'
        board[nx][ny] = 'I'

def solution():
    for i,v in enumerate(direction):
        move_arduino()
