v1, v2 = input().rstrip().split(' ')
v3 = []
for v4 in range(int(v1)):
    v3.append(input())
v3 = sorted(v3)
for v5 in v3:
    print(v5, end='')
