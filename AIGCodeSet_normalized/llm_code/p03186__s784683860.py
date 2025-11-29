v1 = list(map(int, input().split()))
if v1[0] + v1[1] >= v1[2]:
    print(v1[0] + v1[1] + v1[2])
else:
    print(v1[0] + v1[1] + v1[2] - 1)
