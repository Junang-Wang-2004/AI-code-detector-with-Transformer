class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = sum(a1)
        if v1 < a2:
            return -1
        a1.sort()
        v2 = 0
        while a2:
            v3 = a1.pop()
            if v3 <= a2:
                a2 -= v3
                v1 -= v3
            elif v1 - v3 >= a2:
                v1 -= v3
            else:
                a1.append(v3 // 2)
                a1.append(v3 // 2)
                v2 += 1
        return v2
