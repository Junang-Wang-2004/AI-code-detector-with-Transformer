v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = [v2[i] - v3[i] for v5 in range(v1)]
v6 = sum(v4)
if v6 % 2 == 0 and all((x % 2 == 0 for v7 in v4)):
    print('Yes')
else:
    print('No')
