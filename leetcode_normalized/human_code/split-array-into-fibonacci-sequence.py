class C1(object):

    def splitIntoFibonacci(self, a1):
        """
        """

        def startswith(a1, a2, a3):
            v1 = 0
            for v2 in range(a2, len(a1)):
                v1 = 10 * v1 + int(a1[v2])
                if v1 == a3:
                    return v2 - a2 + 1
                elif v1 > a3:
                    break
            return 0
        v1 = 2 ** 31 - 1
        v2 = 0
        for v3 in range(len(a1) - 2):
            v2 = 10 * v2 + int(a1[v3])
            v4 = 0
            for v5 in range(v3 + 1, len(a1) - 1):
                v4 = 10 * v4 + int(a1[v5])
                v6 = [v2, v4]
                v7 = v5 + 1
                while v7 < len(a1):
                    if v6[-2] > v1 - v6[-1]:
                        break
                    v8 = v6[-2] + v6[-1]
                    v9 = startswith(a1, v7, v8)
                    if v9 == 0:
                        break
                    v6.append(v8)
                    v7 += v9
                else:
                    return v6
                if v4 == 0:
                    break
            if v2 == 0:
                break
        return []
