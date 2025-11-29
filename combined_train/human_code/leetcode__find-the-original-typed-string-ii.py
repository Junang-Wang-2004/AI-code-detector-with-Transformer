from functools import reduce

class C1(object):

    def possibleStringCount(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = [0]
        for v3 in range(len(a1)):
            v2[-1] += 1
            if v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]:
                v2.append(0)
        v2.pop()
        v4 = reduce(lambda accu, x: accu * x % v1, v2, 1)
        if a2 <= len(v2):
            return v4
        v5 = [0] * (a2 - len(v2))
        v5[0] = 1
        for v6 in v2:
            for v3 in range(len(v5) - 1):
                v5[v3 + 1] = (v5[v3 + 1] + v5[v3]) % v1
            for v3 in reversed(range(v6, len(v5))):
                v5[v3] = (v5[v3] - v5[v3 - v6]) % v1
        return reduce(lambda accu, x: (accu - x) % v1, v5, v4)
