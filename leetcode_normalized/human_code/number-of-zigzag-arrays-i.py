from functools import reduce

class C1(object):

    def zigZagArrays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        a3 -= a2
        v3 = [1] * (a3 + 1)
        for v4 in range(a1 - 1):
            v5 = 0
            for v6 in range(len(v3)):
                v3[v6], v5 = (v5, (v5 + v3[v6]) % v1)
            v3.reverse()
        return reduce(lambda accu, x: (accu + x) % v1, v3, 0) * 2 % v1
