n = int(input())
d = [0] * 90

d[0] = 1
d[1] = 1
for i in range(2,len(d)):
    d[i] = d[i-1] + d[i-2]

print(d[n-1])