v1 = input()
v2 = int(input())
v3 = ''
for v4 in range(0, len(v1), v2):
    v3 += v1[v4]
print(v3)
