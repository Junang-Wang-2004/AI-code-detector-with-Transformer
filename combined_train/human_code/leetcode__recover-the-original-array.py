import collections

class C1(object):

    def recoverArray(self, a1):
        """
        """

        def check(a1, a2, a3):
            for v1 in a1:
                if a2[v1] == 0:
                    continue
                if a2[v1 + 2 * a1] == 0:
                    return False
                a2[v1] -= 1
                a2[v1 + 2 * a1] -= 1
                a3.append(v1 + a1)
            return True
        a1.sort()
        v1 = collections.Counter(a1)
        for v2 in range(1, len(a1) // 2 + 1):
            v3 = a1[v2] - a1[0]
            if v3 == 0 or v3 % 2:
                continue
            v3 //= 2
            v4 = []
            if check(v3, collections.Counter(v1), v4):
                return v4
        return []
