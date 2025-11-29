class C1(object):

    def incremovableSubarrayCount(self, a1):
        """
        """
        for v1 in reversed(range(1, len(a1))):
            if not a1[v1 - 1] < a1[v1]:
                break
        else:
            return (len(a1) + 1) * len(a1) // 2
        v2 = len(a1) - v1 + 1
        for v3 in range(len(a1) - 1):
            while v1 < len(a1) and (not a1[v3] < a1[v1]):
                v1 += 1
            v2 += len(a1) - v1 + 1
            if not a1[v3] < a1[v3 + 1]:
                break
        return v2
