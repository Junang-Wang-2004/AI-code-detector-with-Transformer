v1 = int(input())
v2 = [int(num) for v3 in input().split()]
v4 = [[v2, []]]

def f1(a1):
    v1, v2 = a1.pop(0)
    v3 = len(v1) - 1
    while v3 >= 0:
        if v1[v3] == v3 + 1:
            del v1[v3]
            v2 = [v3 + 1] + v2
            a1.append([v1, v2])
            break
        v3 -= 1
    return a1
v5 = -1
while v4 != []:
    if v4[-1][0] == []:
        v5 = v4[-1]
        break
    v4 = f1(v4)
if v5 == -1:
    print(v5)
else:
    for v3 in v5[1]:
        print(v3)
