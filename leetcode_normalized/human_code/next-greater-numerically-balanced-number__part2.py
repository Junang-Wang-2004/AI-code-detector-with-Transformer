class C1(object):

    def nextBeautifulNumber(self, a1):
        """
        """

        def next_permutation(a1, a2, a3):

            def reverse(a1, a2, a3):
                v1, v2 = (a2, a3 - 1)
                while v1 < v2:
                    a1[v1], a1[v2] = (a1[v2], a1[v1])
                    v1 += 1
                    v2 -= 1
            v1, v2 = (a2 - 1, a2)
            for v3 in reversed(range(a2, a3 - 1)):
                if a1[v3] < a1[v3 + 1]:
                    v1 = v3
                    break
            else:
                reverse(a1, a2, a3)
                return False
            for v3 in reversed(range(v1 + 1, a3)):
                if a1[v3] > a1[v1]:
                    v2 = v3
                    break
            a1[v1], a1[v2] = (a1[v2], a1[v1])
            reverse(a1, v1 + 1, a3)
            return True
        v1 = [1, 22, 122, 333, 1333, 4444, 14444, 22333, 55555, 122333, 155555, 224444, 666666]
        v2 = list(str(a1))
        v3 = 1224444
        for v4 in v1:
            v4 = list(str(v4))
            if len(v4) < len(v2):
                continue
            if len(v4) > len(v2):
                v3 = min(v3, int(''.join(v4)))
                continue
            while True:
                if v4 > v2:
                    v3 = min(v3, int(''.join(v4)))
                if not next_permutation(v4, 0, len(v4)):
                    break
        return v3
