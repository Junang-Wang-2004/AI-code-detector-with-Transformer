class C1(object):

    def bowlSubarrays(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in range(len(a1)):
            while v2 and a1[v2[-1]] < a1[v3]:
                v2.pop()
                if v2:
                    v1 += 1
            v2.append(v3)
        return v1
