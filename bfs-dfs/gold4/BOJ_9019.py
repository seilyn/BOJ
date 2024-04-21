from collections import deque
import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    start, end = map(int, input().split())
    check = [False for _ in range(10001)]
    queue = deque()
    queue.append([start, ''])
    check[start] = True

    while queue:
        num, cmd = queue.popleft()

        if num == end:
            print(cmd)
            break

        d = (num * 2) % 10000
        if not check[d]:
            check[d] = True
            queue.append([d, cmd + 'D'])

        s = (num-1) % 10000
        if not check[s]:
            check[s] = True
            queue.append([s, cmd+'S'])

        l = num//1000 + (num % 1000) * 10
        if not check[l]:
            check[l] = True
            queue.append([l, cmd+'L'])

        r = (num%10)*1000 + (num//10)
        if not check[r]:
            check[r] = True
            queue.append([r, cmd+'R'])

