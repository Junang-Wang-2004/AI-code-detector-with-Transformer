class C1(object):

    def binarySearchableNumbers(self, a1):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        for v2 in reversed(range(1, len(a1) + 1)):
            v1[v2 - 1] = min(v1[v2], a1[v2 - 1])
        v3, v4 = (set(), float('-inf'))
        for v2 in range(len(a1)):
            if v4 <= a1[v2] <= v1[v2 + 1]:
                v3.add(a1[v2])
            v4 = max(v4, a1[v2])
        return len(v3)
