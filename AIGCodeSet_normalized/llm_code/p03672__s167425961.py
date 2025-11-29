v1 = input()
if len(v1) % 2 != 0:
    v1 = v1 + '?'
for v2 in range(len(v1) - 1, 0, -2):
    if v1[:v2 // 2] == v1[v2 // 2 + 1:v2]:
        print(v2 // 2)
        break
