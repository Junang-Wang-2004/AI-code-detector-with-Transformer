v1 = input()
v2 = int(input())
v3 = ''
if v2 == 1:
    print(v1)
else:
    for v4 in range(len(v1) // v2):
        v3 += v1[v4 * v2]
    if len(v1) % v2 != 0:
        v3 += v1[-1]
print(v3)
