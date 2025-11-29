v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort(reverse=True)
for v3 in range(v1):
    if v2[v3] < 0:
        v4 = v2[:v3]
        v5 = v2[v3:]
        break
    if v3 == v1 - 1:
        v4 = v2
        v5 = []
v6 = 0
v7 = len(v4)
if v7 > 1:
    if v7 % 2 == 0:
        print(abs(sum(v4[:v7 // 2])) - abs(sum(v4[v7 // 2:])) - sum(v5))
        print(v4[0], v4[-1])
        v6 = v4[0] - v4[-1]
        for v3 in range(1, v7 // 2):
            print(v4[-(v3 + 1)], v6)
            v6 = v4[-(v3 + 1)] - v6
            print(v4[v3], v6)
            v6 = v4[v3] - v6
    else:
        print(sum(v4[:v7 // 2]) - sum(v4[v7 // 2 + 1:]) + abs(v4[v7 // 2]) - sum(v5))
        print(v4[-1], v4[0])
        v6 = v4[-1] - v4[0]
        for v3 in range(1, v7 // 2):
            print(v4[v3], v6)
            v6 = v4[v3] - v6
            print(v4[-(v3 + 1)], v6)
            v6 = v4[-(v3 + 1)] - v6
        print(v4[v7 // 2], v6)
elif v7 == 1:
    print(v4[0] - sum(v5))
    print(v4[0], v5[0])
    v6 = v4[0] - v5[0]
else:
    print(-sum(v5) + v5[0] * 2)
    v6 = v5[0]
for v3 in range(len(v5) - 1):
    print(v6, v5[v3 + 1])
    v6 -= v5[v3 + 1]
