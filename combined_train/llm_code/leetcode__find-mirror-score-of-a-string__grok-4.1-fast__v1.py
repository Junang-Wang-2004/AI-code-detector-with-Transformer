class C1(object):

    def calculateScore(self, a1):
        v1 = 0
        v2 = ord('a')
        for v3 in range(13):
            v4 = 25 - v3
            v5 = []
            v6 = []
            for v7, v8 in enumerate(a1):
                v9 = ord(v8) - v2
                if v9 == v3:
                    if v6:
                        v1 += v7 - v6.pop()
                    else:
                        v5.append(v7)
                elif v9 == v4:
                    if v5:
                        v1 += v7 - v5.pop()
                    else:
                        v6.append(v7)
        return v1
