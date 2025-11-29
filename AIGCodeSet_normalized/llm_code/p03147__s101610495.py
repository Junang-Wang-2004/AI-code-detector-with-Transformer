v1 = int(input())
v2 = input().split(' ')
v2 = [int(i) for v3 in v2]
v4 = 0
for v3 in range(v1):
    if v2[v3] > 0:
        v4 += 1
print(v4)
