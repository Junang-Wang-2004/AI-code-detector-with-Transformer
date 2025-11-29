class C1(object):

    def canFormArray(self, a1, a2):
        """
        """
        v1 = {x[0]: i for v2, v3 in enumerate(a2)}
        v2 = 0
        while v2 < len(a1):
            if a1[v2] not in v1:
                return False
            for v4 in a2[v1[a1[v2]]]:
                if v2 == len(a1) or a1[v2] != v4:
                    return False
                v2 += 1
        return True
