v1 = int(input())
v2 = list(map(int, input().split()))
while len(v2) > 1:
    v3 = v2[0]
    for v4 in range(1, len(v2)):
        v2[v4] %= v3
    v2 = [ans for v5 in v2 if v5 > 0]
    v2.sort()
print(v2[0])
