v1 = int(input())
if v1 % 2:
    print(0)
    exit()

def f1(a1, a2):
    a1 -= a1 % (2 * a2)
    return a1 // a2 // 2
v2 = 0
v3 = 1
v4 = 5
while v3:
    v3 = f1(v1, v4)
    v2 += v3
    v4 *= 5
print(v2)
