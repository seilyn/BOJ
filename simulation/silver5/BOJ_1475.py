string = str(input())
visited = [0] * 10
count = 0

for char in string:
    visited[int(char)] += 1


visited[6] = (visited[6] + visited[9] + 1) // 2
visited[9] = 0

count = max(visited)

print(count)
