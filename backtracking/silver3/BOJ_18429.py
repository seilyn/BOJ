import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recur(now, weight):
    global answer
    if now == n:
        answer += 1
        return

    # 3일 동안
    for i in range(n):
        if not visited[i]:
            if kit[i] + weight -k >= 500:
                visited[i] = True
                recur(now+1, weight+kit[i] - k)
                visited[i] = False



n,k = map(int, input().split())
kit = list(map(int, input().split()))
visited = [False] * n
routine = []
answer = 0

recur(1, 500)

print(answer)
