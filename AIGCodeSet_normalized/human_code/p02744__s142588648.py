def f1(a1, a2, a3):
    if len(a1) == a3:
        print(a1)
    else:
        for v1 in range(97, ord(a2) + 1):
            f1(a1 + chr(v1), chr(max(v1 + 1, ord(a2))), a3)
v1 = int(input())
f1('', 'a', v1)
