class C1(object):

    def minimumLength(self, a1):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            if a1[v1] != a1[v2]:
                break
            v3 = a1[v1]
            while v1 <= v2:
                if a1[v1] != v3:
                    break
                v1 += 1
            while v1 <= v2:
                if a1[v2] != v3:
                    break
                v2 -= 1
        return v2 - v1 + 1
