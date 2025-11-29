v1, v2 = map(int, input().split())
v3 = 0
while v1 >= v2 ** v3:
    if v1 >= v2 ** (v3 + 1):
        v3 = v3 + 1
    else:
        break
print(v3 + 1)
