v1, v2 = map(str, input().split())
v3, v4 = map(int, input().split())
v5 = str(input())
if v1 == v5:
    print(v3 - 1, v4)
else:
    print(v3, v4 - 1)
