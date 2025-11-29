from functools import reduce

class C1(object):

    def minimumTotal(self, a1):
        if not a1:
            return 0
        v1 = a1[0] + [float('inf')]
        for v2 in range(1, len(a1)):
            next = []
            next.append(a1[v2][0] + v1[0])
            for v3 in range(1, v2 + 1):
                next.append(a1[v2][v3] + min(v1[v3 - 1], v1[v3]))
            v1 = next + [float('inf')]
        return reduce(min, v1)
