v1 = list(map(int, input().split()))
if max(v1) * 2 == sum(v1):
    print('Yes')
else:
    print('No')
