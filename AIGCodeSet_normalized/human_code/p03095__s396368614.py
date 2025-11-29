from collections import Counter

def f1():
    v1 = int(input())
    v2 = input()
    v3 = Counter(v2)
    v4 = 1
    v5 = 10 ** 9 + 7
    for v6 in v3.values():
        v4 *= v6 + 1
        v4 %= v5
    print(v4 - 1)
if __name__ == '__main__':
    f1()
