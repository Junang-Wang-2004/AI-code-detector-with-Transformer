v1 = list(map(int, input().split()))
for v2 in range(3):
    if v1.count(v1[v2]) == 1:
        print(v1[v2])
        break
