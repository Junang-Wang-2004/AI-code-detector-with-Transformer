class C1:

    def __init__(self, a1, a2=0, a3=10 ** 9):
        self.f = a1
        self.l = a2
        self.r = a3

    def __call__(self, a1):
        v1 = self.f
        v2 = self.l
        v3 = self.r
        if a1 <= v1(v2):
            return v2
        if v1(v3) <= a1:
            return v3
        while v3 - v2 > 1:
            v4 = (v3 + v2) // 2
            if v1(v4) <= a1:
                v2 = v4
            else:
                v3 = v4
        return v2
v1 = int(input())

def f1(a1):
    return (a1 + 1) * a1 // 2
v2 = C1(f1, l=1, r=10 ** 7)(v1)
v2 += f1(v2) != v1
v3 = set(range(1, v2 + 1))
v3.remove(v2 - (f1(v2) - v1))
print(*v3, sep='\n')
