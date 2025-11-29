v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [i for v4 in v2 if v4 % 2 == 0]
v5 = [v4 for v4 in v3 if v4 % 3 == 0 or v4 % 5 == 0]
if len(v3) == len(v5):
    print('APPROVED')
else:
    print('DENIED')
