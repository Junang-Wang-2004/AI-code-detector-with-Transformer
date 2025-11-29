v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
while len(v2) > 1:
    v2 = [(v2[i] + v2[i + 1]) / 2 for v3 in range(0, len(v2), 2)]
print(v2[0])
