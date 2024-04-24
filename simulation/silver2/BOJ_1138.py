import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
queue = [0 for _ in range(n)]
for i in range(n):
    cnt = 0

    for j in range(n):
        if cnt == s[i] and queue[j] == 0:
            queue[j] = i+1
            break
        elif queue[j] == 0:
            cnt+=1


print(*queue)