import sys
input = sys.stdin.readline

n, m = map(int, input().split())
group = dict()
for _ in range(n):
    group_name = str(input().rstrip())
    group_member_count = int(input())

    members = []

    for _ in range(group_member_count):

        members.append(str(input().rstrip()))
        group[group_name] = members



for _ in range(m):
    name = str(input().rstrip())
    kind = int(input())

    # 그룹의 이름
    if kind == 1:
        for k,v in group.items():
            for member in v:
                if member == name:
                    print(k)
    # 그룹의 이름
    elif kind == 0:
        group[name].sort()
        for member in group[name]:
            print(member)
        # print(group[name])
