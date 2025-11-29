v1 = list(map(int, input().split()))
for v2, v3 in enumerate(v1, start=1):
    if v3 == 0:
        print(v2)
        break
