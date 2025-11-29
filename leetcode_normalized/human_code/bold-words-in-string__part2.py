class C1(object):

    def boldWords(self, a1, a2):
        """
        """
        v1 = [0] * len(a2)
        for v2 in a1:
            v3 = a2.find(v2)
            while v3 != -1:
                v1[v3:v3 + len(v2)] = [1] * len(v2)
                v3 = a2.find(v2, v3 + 1)
        v4 = []
        for v5 in range(len(a2)):
            if v1[v5] and (v5 == 0 or not v1[v5 - 1]):
                v4.append('<b>')
            v4.append(a2[v5])
            if v1[v5] and (v5 == len(a2) - 1 or not v1[v5 + 1]):
                v4.append('</b>')
        return ''.join(v4)
