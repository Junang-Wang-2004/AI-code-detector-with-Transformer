import fractions

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v2.sort()
    v3 = v2[0]
    for v4, v5 in enumerate(v2, 1):
        if v3 == v5:
            continue
        elif v3 % v5 == 0 or v5 % v3 == 0:
            v3 = min(v3, fractions.gcd(v3, v5))
        elif v3 % 2 == 0 and v5 % 2 == 0:
            v3 = 2
        else:
            v3 = v5
    print(v3)
if __name__ == '__main__':
    f1()
