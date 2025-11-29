v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = sorted(v2)
for v5 in range(v1):
    if v2[v5] == v4[-1]:
        print(v4[-2])
    else:
        print(v4[-1])
