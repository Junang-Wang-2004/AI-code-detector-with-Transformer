v1 = int(input())
list = list(map(str, input().split()))
v2 = []
for v3 in range(1, v1 - 2):
    v2.append(list.count(str(v3)))
v4 = '\n'.join(v2)
print(v4)
