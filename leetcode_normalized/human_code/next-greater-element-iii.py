class C1(object):

    def nextGreaterElement(self, a1):
        """
        """
        v1 = list(map(int, list(str(a1))))
        v2, v3 = (-1, 0)
        for v4 in range(len(v1) - 1):
            if v1[v4] < v1[v4 + 1]:
                v2 = v4
        if v2 == -1:
            v1.reverse()
            return -1
        for v4 in range(v2 + 1, len(v1)):
            if v1[v4] > v1[v2]:
                v3 = v4
        v1[v2], v1[v3] = (v1[v3], v1[v2])
        v1[v2 + 1:] = v1[:v2:-1]
        v5 = int(''.join(map(str, v1)))
        return -1 if v5 >= 2147483647 else v5
