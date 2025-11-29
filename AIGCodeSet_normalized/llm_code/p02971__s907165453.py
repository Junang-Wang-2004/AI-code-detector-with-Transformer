v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
for v3 in range(v1):
    v4 = v2[:v3] + v2[v3 + 1:]
    print(max(v4))
