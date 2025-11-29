import itertools

class C1(object):

    def largestTimeFromDigits(self, a1):
        """
        """
        v1 = ''
        for v2 in range(len(a1)):
            a1[v2] *= -1
        a1.sort()
        for v3, v4, v5, v6 in itertools.permutations(a1):
            v7 = -(10 * v3 + v4)
            v8 = -(10 * v5 + v6)
            if 0 <= v7 < 24 and 0 <= v8 < 60:
                v1 = '{:02}:{:02}'.format(v7, v8)
                break
        return v1
