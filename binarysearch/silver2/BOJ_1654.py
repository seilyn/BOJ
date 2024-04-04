import sys
input = sys.stdin.readline

n,k = map(int, input().split())
cables = [int(input()) for _ in range(n)]

s = 1
e = max(cables)
max_count = 0
while s <= e:

    count = 0

    # 1, 802 -> 401
    mid = (s + e) // 2

    for cable in cables:
        count += (cable // mid)


    if count >= k:
        s = mid + 1
    else:
        e = mid - 1
print(e)
