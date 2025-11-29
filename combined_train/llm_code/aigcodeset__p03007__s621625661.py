v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = []
v4 = []
for v5 in v2:
    if v5 >= 0:
        v3.append(v5)
    else:
        v4.append(v5)
v4.reverse()
v6 = []
while len(v3) > 0 and len(v4) > 0:
    if v3[-1] > abs(v4[-1]):
        v6.append((v3.pop(), v4.pop()))
    else:
        v6.append((v4.pop(), v3.pop()))
while len(v3) > 1:
    v6.append((v3.pop(), v3.pop()))
while len(v4) > 1:
    v6.append((v4.pop(), v4.pop()))
print(v6[-1][1] - v6[-1][0])
for v7 in range(v1 - 2):
    print(v6[v7][0], v6[v7][1])
print(v6[-1][1], v6[-1][0])
