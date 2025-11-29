v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1, a2):
    if not a1 % a2:
        return a2
    return f1(a2, a1 % a2)
v3, v4 = ([v2[0]], [v2[-1]])
for v5 in v2[1:]:
    v3 += [f1(v3[-1], v5)]
for v5 in v2[::-1][1:]:
    v4 += [f1(v4[-1], v5)]
v4 = v4[::-1]
v6 = max(v3[-2], v4[-2])
for v7 in range(2, v1):
    v6 = max(v6, f1(v3[v7 - 2], v4[v7]))
print(v6)
