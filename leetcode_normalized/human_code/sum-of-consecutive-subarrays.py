from functools import reduce

class C1(object):

    def getSum(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def count(a1):
            v1 = v2 = v3 = 0
            for v4 in range(len(a1)):
                v3 += 1
                v2 = (v2 + a1[v4] * v3) % v1
                v1 = (v1 + v2) % v1
                if v4 + 1 < len(a1) and a1[v4 + 1] - a1[v4] == a1:
                    continue
                v2 = v3 = 0
            return v1
        return (count(1) + count(-1) - reduce(lambda accu, x: (accu + x) % v1, a1, 0)) % v1
