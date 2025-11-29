v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v4 = sum(v2)
if v4 % 10 == 0:
    v5 = True
    v2.sort()
    for v6 in v2:
        if v6 % 10 != 0:
            print(v4 - v6)
            v5 = False
            break
    if v5:
        print(0)
else:
    print(v4)
