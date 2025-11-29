class C1(object):

    def confusingNumberII(self, a1):
        """
        """
        v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        v2 = {'0': '0', '1': '1', '8': '8'}

        def totalCount(a1):
            v1 = str(a1)
            v2 = 0
            v3 = len(v1) ** (len(v1) - 1)
            for v4 in range(len(v1) + 1):
                if v4 == len(v1):
                    v2 += 1
                    break
                v5 = sum((int(c < v1[v4]) for v6 in v1.keys()))
                v2 += v5 * v3
                if v1[v4] not in v1:
                    break
                v3 //= len(v1)
            return v2 - 1

        def validCountInLessLength(a1):
            v1 = str(a1)
            v2 = 0
            v3 = len(v2)
            for v4 in range(1, len(v1), 2):
                if v4 == 1:
                    v2 += len({c for v5 in v2.keys() if v5 != '0'})
                else:
                    v2 += v3 * (len(v1) - 1)
                    v3 *= len(v1)
            v3 = 1
            for v4 in range(2, len(v1), 2):
                v2 += v3 * (len(v1) - 1)
                v3 *= len(v1)
            return v2

        def validCountInFullLength(a1):
            v1 = str(a1)
            v2 = v1[:(len(v1) + 1) // 2]
            v3 = 0
            v4 = v2 if len(v1) % 2 else v1
            v5 = int(len(v1) ** (len(v2) - 2) * len(v4))
            for v6 in range(len(v2)):
                if v6 == len(v2) - 1:
                    v3 += sum((int(c < v2[v6]) for v7 in v4.keys() if v6 != 0 or v7 != '0'))
                    if v2[v6] not in v4:
                        break
                    v8 = list(v2) + [v1[v2[v6]] for v6 in reversed(range(len(v2) - len(v1) % 2))]
                    v3 += 0 < int(''.join(v8)) <= a1
                    break
                v9 = sum((int(v7 < v2[v6]) for v7 in v1.keys() if v6 != 0 or v7 != '0'))
                v3 += v9 * v5
                if v2[v6] not in v1:
                    break
                v5 //= len(v1)
            return v3
        return totalCount(a1) - validCountInLessLength(a1) - validCountInFullLength(a1)
