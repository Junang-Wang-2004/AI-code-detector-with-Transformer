import itertools

def f1(a1):
    v1 = 0
    for v2 in itertools.product(range(10), repeat=a1):
        if any((x == 0 for v3 in v2)) and any((v3 == 9 for v3 in v2)):
            v1 += 1
    return v1 % (10 ** 9 + 7)
v1 = int(input())
print(f1(v1))
