class C1(object):

    def plusOne(self, a1):
        """
        """
        v1 = a1[::-1]
        v2 = 1
        for v3 in range(len(v1)):
            v1[v3] += v2
            v2, v1[v3] = divmod(v1[v3], 10)
        if v2:
            v1.append(v2)
        return v1[::-1]
