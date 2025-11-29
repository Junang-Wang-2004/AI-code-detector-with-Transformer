from functools import reduce
v1 = [0] * 2

class C1(object):

    def countKReducibleNumbers(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def popcount(a1):
            return bin(a1).count('1')
        while len(a1) - 1 >= len(v1):
            v1.append(v1[popcount(len(v1))] + 1)
        v2 = [0] * len(a1)
        v3 = 0
        for v4 in range(len(a1)):
            for v5 in reversed(list(range(v4))):
                v2[v5 + 1] = (v2[v5 + 1] + v2[v5]) % v1
            if a1[v4] != '1':
                continue
            v2[v3] = (v2[v3] + 1) % v1
            v3 += 1
        return reduce(lambda accu, x: (accu + x) % v1, (v2[v4] for v4 in range(1, len(a1)) if v1[v4] < a2), 0)
