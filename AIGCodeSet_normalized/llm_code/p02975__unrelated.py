v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in range(v1):
    if v2[v3] ^ v2[(v3 + 1) % v1] != v2[(v3 + 2) % v1]:
        print('No')
        exit()
print('Yes')
