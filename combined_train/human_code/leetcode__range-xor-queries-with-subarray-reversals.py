import random

class C1(object):
    __slots__ = ('value', 'prior', 'cnt', 'xor_sum', 'rev', 'l', 'r')

    def __init__(self, a1):
        self.value = a1
        self.prior = random.randint(1, 1 << 30)
        self.cnt = 1
        self.xor_sum = a1
        self.rev = False
        self.l = None
        self.r = None

def f1(a1):
    return a1.cnt if a1 else 0

def f2(a1):
    return a1.xor_sum if a1 else 0

def f3(a1):
    if a1:
        a1.cnt = 1 + f1(a1.l) + f1(a1.r)
        a1.xor_sum = a1.value ^ f2(a1.l) ^ f2(a1.r)

def f4(a1):
    if a1 and a1.rev:
        a1.rev = False
        a1.l, a1.r = (a1.r, a1.l)
        if a1.l:
            a1.l.rev ^= True
        if a1.r:
            a1.r.rev ^= True

def f5(a1, a2):
    f4(a1)
    f4(a2)
    if not a1 or not a2:
        return a1 or a2
    if a1.prior > a2.prior:
        a1.r = f5(a1.r, a2)
        f3(a1)
        return a1
    else:
        a2.l = f5(a1, a2.l)
        f3(a2)
        return a2

def f6(a1, a2, a3=0):
    if not a1:
        return (None, None)
    f4(a1)
    v1 = a3 + f1(a1.l)
    if a2 <= v1:
        v2, a1.l = f6(a1.l, a2, a3)
        f3(a1)
        return (v2, a1)
    else:
        a1.r, v3 = f6(a1.r, a2, a3 + 1 + f1(a1.l))
        f3(a1)
        return (a1, v3)

def f7(a1, a2, a3):
    v1, v2 = f6(a1, a2)
    v2, v3 = f6(v2, a3 - a2 + 1)
    if v2:
        v2.rev ^= True
    return f5(f5(v1, v2), v3)

def f8(a1):
    if not a1:
        return
    v1 = a1
    if a1.l and a1.l.prior > v1.prior:
        v1 = a1.l
    if a1.r and a1.r.prior > v1.prior:
        v1 = a1.r
    if v1 != a1:
        a1.prior, v1.prior = (v1.prior, a1.prior)
        f8(v1)

def f9(a1, a2, a3):
    if not a3:
        return None
    v1 = a3 // 2
    v2 = C1(a1[a2 + v1])
    v2.l = f9(a1, a2, v1)
    v2.r = f9(a1, a2 + v1 + 1, a3 - v1 - 1)
    f8(v2)
    f3(v2)
    return v2

class C2(object):

    def getResults(self, a1, a2):
        """
        """

        def update(a1, a2, a3):
            v1, v2 = f6(a1, a2)
            v2, v3 = f6(v2, 1)
            v2.value = a3
            f3(v2)
            return f5(f5(v1, v2), v3)

        def query(a1, a2, a3):
            v1, v2 = f6(a1, a2)
            v2, v3 = f6(v2, a3 - a2 + 1)
            v4 = f2(v2)
            return (f5(f5(v1, v2), v3), v4)
        v1 = []
        v2 = f9(a1, 0, len(a1))
        for v3 in a2:
            if v3[0] == 1:
                v2 = update(v2, v3[1], v3[2])
            elif v3[0] == 2:
                v2, v4 = query(v2, v3[1], v3[2])
                v1.append(v4)
            elif v3[0] == 3:
                v2 = f7(v2, v3[1], v3[2])
        return v1
