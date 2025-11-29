v1 = list(input())
v2 = len(v1) // 2
for v3 in range(1, len(v1) // 2):
    v1.pop()
    v1.pop()
    if v1[:len(v1) // 2] == v1[len(v1) // 2:]:
        print(len(v1))
        break
