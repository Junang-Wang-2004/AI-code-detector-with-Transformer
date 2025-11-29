class C1(object):

    def findLexSmallestString(self, a1, a2, a3):
        """
        """

        def less(a1, a2, a3):
            for v1 in range(len(a1)):
                if a1[(v1 + a2) % len(a1)] != a1[(v1 + a3) % len(a1)]:
                    return a1[(v1 + a2) % len(a1)] < a1[(v1 + a3) % len(a1)]
            return False
        a1 = list(a1)
        v2 = a1[:]
        v3 = [False] * 10
        while not v3[int(a1[0])]:
            v3[int(a1[0])] = True
            v4 = [False] * 10
            while not v4[int(a1[1])]:
                v4[int(a1[1])] = True
                v5 = 0
                v6 = [False] * len(a1)
                v7 = a3
                while not v6[v7]:
                    v6[v7] = True
                    if less(a1, v7, v5):
                        v5 = v7
                    v7 = (v7 + a3) % len(a1)
                v2 = min(v2, a1[v5:] + a1[:v5])
                for v8 in range(1, len(a1), 2):
                    a1[v8] = str((int(a1[v8]) + a2) % 10)
            if a3 % 2:
                for v8 in range(0, len(a1), 2):
                    a1[v8] = str((int(a1[v8]) + a2) % 10)
        return ''.join(v2)
