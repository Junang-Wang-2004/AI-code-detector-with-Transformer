v1 = list(input().replace('BC', 'Z'))[::-1]
v2 = 0

def f1(a1):
    v1 = 0
    v2 = len(a1) - 1
    for v3, v4 in enumerate(a1):
        if v4 == 'A':
            v1 += v2 - v3
            v2 -= 1
    return v1
v3 = []
while v1:
    v4 = v1.pop(-1)
    if v4 == 'B' or v4 == 'C':
        v2 += f1(v3)
        v3.clear()
    else:
        v3.append(v4)
print(v2 + f1(v3))
