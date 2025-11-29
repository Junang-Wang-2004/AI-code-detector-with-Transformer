class C1(object):

    def resultArray(self, a1):
        """
        """
        v1, v2 = ([a1[0]], [a1[1]])
        for v3 in range(2, len(a1)):
            if v1[-1] > v2[-1]:
                v1.append(a1[v3])
            else:
                v2.append(a1[v3])
        return v1 + v2
