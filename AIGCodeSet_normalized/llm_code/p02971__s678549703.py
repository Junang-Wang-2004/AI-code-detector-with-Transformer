v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = max(v2)
for v3 in range(v1):
    if v4 >= v2[v3]:
        print(v4)
    else:
        print(v2[v3])
