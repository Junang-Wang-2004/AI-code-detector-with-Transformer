class C1(object):

    def findSubarrays(self, a1):
        """
        """
        v1 = set()
        for v2 in range(len(a1) - 1):
            if a1[v2] + a1[v2 + 1] in v1:
                return True
            v1.add(a1[v2] + a1[v2 + 1])
        return False
