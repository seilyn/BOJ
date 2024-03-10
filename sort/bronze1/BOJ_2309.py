import sys
sys.setrecursionlimit(10**6)
peoples = []
for _ in range(9):
    peoples.append(int(input()))

selected = [False] * 9
temp = []
found = False

def search(idx, count):
    global found
    if count == 7:
        if sum(temp) == 100 and not found:
            temp.sort()
            for t in temp:
                print(t)
                found = True
        return

    for i in range(idx, len(peoples)):
        if not selected[i]:
            selected[i] = True
            temp.append(peoples[i])
            search(i+1, count+1)
            selected[i] = False
            temp.pop()

search(0, 0)
