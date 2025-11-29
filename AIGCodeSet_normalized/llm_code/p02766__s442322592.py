v1, v2 = map(int, input().split())
for v3 in range(0, v1):
    if v2 ** v3 > v1:
        print(v3 - 1)
        break
