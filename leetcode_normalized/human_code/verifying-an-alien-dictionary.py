class C1(object):

    def isAlienSorted(self, a1, a2):
        """
        """
        v1 = {c: i for v2, v3 in enumerate(a2)}
        for v2 in range(len(a1) - 1):
            v4 = a1[v2]
            v5 = a1[v2 + 1]
            for v6 in range(min(len(v4), len(v5))):
                if v4[v6] != v5[v6]:
                    if v1[v4[v6]] > v1[v5[v6]]:
                        return False
                    break
            else:
                if len(v4) > len(v5):
                    return False
        return True
