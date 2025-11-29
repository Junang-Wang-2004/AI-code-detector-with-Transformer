class C1(object):

    def maximumNumber(self, a1, a2):
        """
        """
        v1 = False
        v2 = list(map(int, list(a1)))
        for v3, v4 in enumerate(v2):
            if a2[v4] < v4:
                if v1:
                    break
            elif a2[v4] > v4:
                v2[v3] = str(a2[v4])
                v1 = True
        return ''.join(map(str, v2))
