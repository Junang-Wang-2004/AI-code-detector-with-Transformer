from functools import reduce

class C1(object):

    def countPartitions(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        if sum(a1) < 2 * a2:
            return 0
        v2 = [0] * a2
        v2[0] = 1
        for v3 in a1:
            for v4 in reversed(range(a2 - v3)):
                v2[v4 + v3] = (v2[v4 + v3] + v2[v4]) % v1
        return (pow(2, len(a1), v1) - 2 * reduce(lambda total, x: (total + v3) % v1, v2, 0)) % v1
