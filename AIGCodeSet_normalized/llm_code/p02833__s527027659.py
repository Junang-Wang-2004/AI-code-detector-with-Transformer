v1 = int(input())
if v1 < 10 or v1 % 2 != 0:
    print(0)

def f1(a1):
    v1 = str(a1)
    v2 = 0
    for v3 in v1:
        if v3 == '0':
            v2 += 1
    return v2
v2 = 0
v3 = 10
while v1 >= 10:
    if v1 / 10 >= 10:
        v2 += v3
        v3 *= 10
    v1 = v1 // 10
print(v2 + int(v1))
