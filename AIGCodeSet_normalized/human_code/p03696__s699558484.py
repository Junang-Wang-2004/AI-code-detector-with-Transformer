v1 = int(input())
v2 = input()
while True:
    v3 = 0
    for v4 in range(len(v2)):
        if v2[v4] == '(':
            v3 += 1
        else:
            v3 -= 1
        if v3 < 0:
            v2 = '(' + v2
            break
    if v3 > 0:
        v2 = v2 + ')'
    if v3 == 0:
        print(v2)
        break
