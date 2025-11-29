v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
max = sum(v2)
for v3 in range(v1):
    if max % 10 != 0:
        print(max)
        exit(0)
    elif (max - v2[v3]) % 10 != 0:
        print(max - v2[v3])
        exit(0)
print('0')
