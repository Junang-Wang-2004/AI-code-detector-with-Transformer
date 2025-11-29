class C1(object):

    def countTexts(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1] * 5
        for v3 in range(1, len(a1) + 1):
            v2[v3 % 5] = 0
            for v4 in reversed(range(max(v3 - (4 if a1[v3 - 1] in '79' else 3), 0), v3)):
                if a1[v4] != a1[v3 - 1]:
                    break
                v2[v3 % 5] = (v2[v3 % 5] + v2[v4 % 5]) % v1
        return v2[len(a1) % 5]
