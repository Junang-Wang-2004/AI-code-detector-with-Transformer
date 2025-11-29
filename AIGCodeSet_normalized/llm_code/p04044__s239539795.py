v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(input())
v3.sort()
print(''.join(v3))
