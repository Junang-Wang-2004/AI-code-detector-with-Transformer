import bisect
import itertools
v1 = 16
v2 = []

def f1():
    v1 = set()
    for v2 in range(1, 512):
        v3 = []
        v4 = None
        v5 = True
        for v6 in range(9):
            if v2 & 1 << v6 != 0:
                v7 = v6 + 1
                v8 = v7 // 2
                v3 += [str(v7)] * v8
                if v7 % 2 != 0:
                    if v4 is not None:
                        v5 = False
                        break
                    v4 = str(v7)
        if not v5:
            continue
        v9 = len(v3)
        v10 = 2 * v9 + (1 if v4 else 0)
        if v10 > v1:
            continue
        for v11 in set(itertools.permutations(v3)):
            v12 = ''.join(v11)
            v13 = v12 + (v4 or '') + v12[::-1]
            v1.add(int(v13))
    global SPECIAL_NUMBERS
    v2[:] = sorted(v1)
f1()

class C1(object):

    def specialPalindrome(self, a1):
        v1 = bisect.bisect_right(v2, a1)
        return v2[v1]
