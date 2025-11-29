class C1(object):

    def search(self, a1, a2):
        """
        """
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if a1[v3] > a2:
                v2 = v3 - 1
            elif a1[v3] < a2:
                v1 = v3 + 1
            else:
                return v3
        return -1
