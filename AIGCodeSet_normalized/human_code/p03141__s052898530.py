v1 = int(input())
v2 = []
v3 = 0
v4 = 0
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v2.append([v6, v7])
v2.sort(key=lambda x: x[0] + x[1], reverse=True)
while True:
    if len(v2) == 0:
        break
    v3 += v2.pop(0)[0]
    if len(v2) == 0:
        break
    v4 += v2.pop(0)[1]
print(v3 - v4)
