v1, v2 = input().split()
v3, v4 = map(int, input().split())
v5 = input()
if v1 == v5:
    print(v3 - 1, v4, sep=' ')
else:
    print(v3, v4 - 1, sep=' ')
