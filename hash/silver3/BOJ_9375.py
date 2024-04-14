

case = int(input())
for _ in range(case):
    n = int(input())
    clothes = dict()

    for _ in range(n):
        name, kind = map(str, input().rstrip().split())

        if kind not in clothes:
            clothes[kind] = [name]
        else:
            clothes[kind].append(name)

    cnt = 1

    for k, v in clothes.items():
        cnt = cnt * (len(v)+1)

    print(cnt-1)

