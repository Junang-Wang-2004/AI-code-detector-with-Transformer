class C1(object):

    def findReplaceString(self, a1, a2, a3, a4):
        """
        """
        v1 = [None] * len(a1)
        for v2 in range(len(a2)):
            if all((a2[v2] + k < len(a1) and a1[a2[v2] + k] == a3[v2][k] for v3 in range(len(a3[v2])))):
                v1[a2[v2]] = (len(a3[v2]), list(a4[v2]))
        v4 = []
        v2 = 0
        while v2 < len(a1):
            if v1[v2]:
                v4.extend(v1[v2][1])
                v2 += v1[v2][0]
            else:
                v4.append(a1[v2])
                v2 += 1
        return ''.join(v4)
