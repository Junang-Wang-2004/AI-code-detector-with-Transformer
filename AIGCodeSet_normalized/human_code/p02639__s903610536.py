v1 = list(map(int, input().split()))
for v2 in range(len(v1)):
    if v1[v2] == 0:
        print(v2 + 1)
