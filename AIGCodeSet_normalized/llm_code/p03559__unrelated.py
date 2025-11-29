v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v2.sort()
v3.sort()
v4.sort()
v5 = 0
v6 = 0
v7 = 0
v8 = 0
while v6 < v1 and v7 < v1 and (v8 < v1):
    if v3[v7] > v2[v6] and v4[v8] > v3[v7]:
        v5 += (v1 - v8) * (v1 - v7)
        v6 += 1
    elif v3[v7] <= v2[v6]:
        v6 += 1
    else:
        v7 += 1
print(v5)
