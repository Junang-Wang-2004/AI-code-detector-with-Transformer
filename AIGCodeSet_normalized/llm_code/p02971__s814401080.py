v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v2.sort()
for v4 in range(v1):
    if v2[v4] == v2[-1]:
        print(v2[-2])
    else:
        print(v2[-1])
