v1 = input()
v2 = int(input())
v3 = 0
for v4 in v1:
    if v4 == '1':
        v3 += 1
    else:
        break
if v3 >= v2:
    print(1)
else:
    print(v1[v3 + 1 - 1])
