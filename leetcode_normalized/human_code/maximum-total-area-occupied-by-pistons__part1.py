import itertools

class C1(object):

    def maxArea(self, a1, a2, a3):
        """
        """
        v1 = [0] * (2 * a1 + 1)
        for v2, v3 in zip(a3, a2):
            if v2 == 'U':
                v1[a1 - v3] -= 1
                v1[a1 - v3 + a1] += 1
            else:
                v1[v3] += 1
                v1[v3 + a1] -= 1
        v4 = v5 = sum(a2)
        v6 = a3.count('U')
        for v7 in range(1, len(v1)):
            v5 += -(len(a3) - v6) + v6
            v4 = max(v4, v5)
            v6 += v1[v7]
        return v4
