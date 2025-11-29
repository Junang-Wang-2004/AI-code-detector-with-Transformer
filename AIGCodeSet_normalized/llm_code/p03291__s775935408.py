v1 = input()
v2 = 10 ** 9 + 7

def f1(a1, a2, a3):
    if a1 == len(a3):
        return 1 if a2 == 3 else 0
    if a3[a1] == '?':
        v1 = 3 * f1(a1 + 1, a2, a3)
        if a2 < 3:
            v1 += f1(a1 + 1, a2 + 1, a3)
    elif a2 < 3 and a3[a1] == 'ABC'[a2]:
        v1 = f1(a1 + 1, a2, a3) + f1(a1 + 1, a2 + 1, a3)
    else:
        v1 = f1(a1 + 1, a2, a3)
    return v1 % v2
print(f1(0, 0, v1))
