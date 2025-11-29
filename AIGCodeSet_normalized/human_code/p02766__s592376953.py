v1, v2 = map(int, input().split())
v3 = ''
while v1 >= v2:
    v3 = v3 + str(v1 % v2)
    v1 = v1 // v2
v3 = v3 + str(v1)
print(len(v3))
