v1, v2 = map(int, input().split())
'\n\u3000\u3000レベルnの層数：a_0 = 1 , a_n = 2*a_(n-1)+3\nレベルnのパティ数：b_0 = 1 , b_n = 2*b_(n-1)+1\n'

def f1(a1):
    if a1 == 0:
        return 1
    else:
        return 2 * f1(a1 - 1) + 3

def f2(a1):
    if a1 == 0:
        return 1
    else:
        return 2 * f2(a1 - 1) + 1

def f3(a1, a2):
    if a2 == 1:
        return 0
    if 1 < a2 <= f1(a1 - 1) + 1:
        return f3(a1 - 1, a2 - 1)
    if a2 == f1(a1 - 1) + 2:
        return f2(a1 - 1) + 1
    if f1(a1 - 1) + 2 < a2 <= 2 * f1(a1 - 1) + 3:
        return f2(a1 - 1) + 1 + f3(a1 - 1, a2 - 2 - f1(a1 - 1))
    if a2 == f1(a1 - 1) + 3:
        return 2 * f2(a1 - 1) + 1
print(f3(v1, v2))
