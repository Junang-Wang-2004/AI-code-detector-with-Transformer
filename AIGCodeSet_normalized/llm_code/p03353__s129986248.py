v1 = input()
v2 = int(input())
v3 = []
for v4 in range(len(v1), 0, -1):
    v5 = len(v1)
    v6 = []
    while v5 - v4 >= 0:
        v6.append(v1[v5 - v4:v5])
        v5 -= 1
    v6 = list(set(v6))
    v6.sort(reverse=True)
    v3.extend(v6)
    if len(v3) >= v2:
        break
print(v3[v2 - 1])
