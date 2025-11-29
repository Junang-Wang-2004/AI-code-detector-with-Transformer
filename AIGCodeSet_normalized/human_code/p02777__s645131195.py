v1, v2 = map(str, input().split())
v3, v4 = map(int, input().split())
v5 = str(input())
if v5 == v1:
    v3 -= 1
else:
    v4 -= 1
print(v3, v4)
