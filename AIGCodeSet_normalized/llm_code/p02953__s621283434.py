v1 = int(input())
v2 = list(map(int, input().split()))
v3 = True
for v4 in range(v1 - 1):
    if v2[v4] > v2[v4 + 1]:
        v2[v4] -= 1
        if v2[v4] > v2[v4 + 1]:
            v3 = False
            break
print('Yes' if v3 else 'No')
