import collections

class C1(object):

    def lemonadeChange(self, a1):
        """
        """
        v1 = [20, 10, 5]
        v2 = collections.defaultdict(int)
        for v3 in a1:
            v2[v3] += 1
            v4 = v3 - v1[-1]
            for v5 in v1:
                if v4 == 0:
                    break
                if v4 >= v5:
                    v6 = min(v2[v5], v4 // v5)
                    v2[v5] -= v6
                    v4 -= v5 * v6
            if v4 != 0:
                return False
        return True
