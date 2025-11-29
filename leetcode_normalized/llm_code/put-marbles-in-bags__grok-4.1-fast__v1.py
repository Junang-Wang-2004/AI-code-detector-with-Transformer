class C1(object):

    def putMarbles(self, a1, a2):
        v1 = [a1[i] + a1[i + 1] for v2 in range(len(a1) - 1)]
        v1.sort()
        v3 = a2 - 1
        return sum(v1[-v3:]) - sum(v1[:v3])
