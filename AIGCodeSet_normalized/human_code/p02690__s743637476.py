v1 = int(input())

def f1(a1):
    for v1 in range(0, 1000)[::-1]:
        for v2 in range(-1000, 1000)[::-1]:
            if v1 ** 5 - v2 ** 5 == a1:
                return (v1, v2)
v2, v3 = f1(v1)
print(v2, v3)
