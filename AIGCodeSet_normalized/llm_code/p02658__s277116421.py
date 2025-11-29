v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in v2:
    v3 *= v4
    if v3 > 10 ** 18:
        print('-1')
        break
else:
    print(v3)
