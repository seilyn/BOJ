n = int(input())
scores = []
for _ in range(n):

    name, a, b, c = map(str,input().strip().split())
    score = [name, int(a), int(b), int(c)]

    scores.append(score)

s = sorted(scores, key=lambda x: [-x[1], x[2], -x[3], x[0]])
for i in s:
    print(i[0])