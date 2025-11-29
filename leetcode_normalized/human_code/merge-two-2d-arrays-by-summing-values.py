class C1(object):

    def mergeArrays(self, a1, a2):
        """
        """
        v1 = []
        v2 = v3 = 0
        while v2 < len(a1) or v3 < len(a2):
            if v3 == len(a2) or (v2 < len(a1) and a1[v2][0] < a2[v3][0]):
                if v1 and v1[-1][0] == a1[v2][0]:
                    v1[-1][1] += a1[v2][1]
                else:
                    v1.append(a1[v2])
                v2 += 1
            else:
                if v1 and v1[-1][0] == a2[v3][0]:
                    v1[-1][1] += a2[v3][1]
                else:
                    v1.append(a2[v3])
                v3 += 1
        return v1
