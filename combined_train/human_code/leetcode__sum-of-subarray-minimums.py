import itertools

class C1(object):

    def sumSubarrayMins(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = ([0] * len(a1), [])
        for v4 in range(len(a1)):
            v5 = 1
            while v3 and v3[-1][0] > a1[v4]:
                v5 += v3.pop()[1]
            v2[v4] = v5
            v3.append([a1[v4], v5])
        v6, v7 = ([0] * len(a1), [])
        for v4 in reversed(range(len(a1))):
            v5 = 1
            while v7 and v7[-1][0] >= a1[v4]:
                v5 += v7.pop()[1]
            v6[v4] = v5
            v7.append([a1[v4], v5])
        return sum((a * l * r for v8, v9, v10 in zip(a1, v2, v6))) % v1
