v1, v2 = map(int, input().split())
list = []
for v3 in range(v1):
    v4 = input()
    list.append(v4)
v5 = sorted(list)
v6 = ''.join(v5)
print(v6)
