v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v2.reverse()
for v3 in range(v1):
    if v2[v3] != v2[0]:
        print(v2[0])
    else:
        print(v2[1])
