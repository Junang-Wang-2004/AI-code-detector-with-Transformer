v1 = int(input())
v2 = [i for v3 in range(50)]

def f1(a1, a2):
    a1[a2] += 49
    for v1 in range(50):
        if v1 == a2:
            continue
        else:
            a1[v1] -= 1
v4 = v1 // 50
v5 = v1 - v4 * 50
for v3 in range(50):
    v2[v3] += v4
for v3 in range(v5):
    f1(v2, v3)
for v3 in range(49):
    print(v2[v3], ' ')
print(v2[-1])
