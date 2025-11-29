v1 = input()
v2 = int(input())
v3 = []
v4 = ''
for v5 in range(0, len(v1) // v2):
    v3.append(v1[v2 * v5:v2 * (v5 + 1)])
if len(v1) % v2 != 0:
    v3.append(v1[len(v1) - v2 + 1:])
for v5 in range(len(v3)):
    v4 += v3[v5][0]
print(v4)
