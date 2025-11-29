v1 = int(input())
v2 = list(map(int, input().split()))
for v3 in range(1, v1):
    if v2[v3 - 1] < v2[v3]:
        v2[v3] -= 1
    if v2[v3 - 1] > v2[v3]:
        print('No')
        break
else:
    print('Yes')
