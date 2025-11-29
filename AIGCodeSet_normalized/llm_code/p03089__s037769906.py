v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v5 = 1
    if v5 < len(v2):
        while v2[v5] == v5 + 1:
            v5 += 1
            if v5 == len(v2):
                break
    if v2[v5 - 1] == v5:
        del v2[v5 - 1]
        v3.append(v5)
    else:
        print(-1)
        import sys
        sys.exit()
for v4 in range(len(v3) - 1, -1, -1):
    print(v3[v4])
