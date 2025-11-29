class C1(object):

    def numberOfSubarrays(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in a1:
            while v2 and v2[-1][0] < v3:
                v2.pop()
            if not v2 or v2[-1][0] != v3:
                v2.append([v3, 0])
            v2[-1][1] += 1
            v1 += v2[-1][1]
        return v1
