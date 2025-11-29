class C1(object):

    def validSubarrays(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in a1:
            while v2 and v2[-1] > v3:
                v2.pop()
            v2.append(v3)
            v1 += len(v2)
        return v1
