class C1(object):

    def minimalKSum(self, a1, a2):
        """
        """
        v1 = v2 = 0
        a1.append(float('inf'))
        for v3 in sorted(set(a1)):
            if not a2:
                break
            v4 = min(v3 - 1 - v2, a2)
            a2 -= v4
            v1 += (v2 + 1 + (v2 + v4)) * v4 // 2
            v2 = v3
        return v1
