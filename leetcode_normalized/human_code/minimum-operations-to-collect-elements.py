class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = [False] * a2
        for v2 in reversed(range(len(a1))):
            if a1[v2] > len(v1) or v1[a1[v2] - 1]:
                continue
            v1[a1[v2] - 1] = True
            a2 -= 1
            if not a2:
                break
        return len(a1) - v2
