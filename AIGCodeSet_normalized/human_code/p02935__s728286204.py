v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
while len(v2) > 1:
    v3 = v2.pop(0)
    v4 = v2.pop(0)
    v5 = (v3 + v4) / 2
    v2.append(v5)
    v2.sort()
print(v2[0])
