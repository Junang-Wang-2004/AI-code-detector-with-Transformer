class C1(object):

    def shortestBeautifulSubstring(self, a1, a2):
        """
        """

        def check(a1, a2):
            if a1[1] - a1[0] + 1 > a2[1] - a2[0] + 1:
                return False
            if a1[1] - a1[0] + 1 < a2[1] - a2[0] + 1:
                return True
            for v1, v2 in zip(range(a1[0], a1[1] + 1), range(a2[0], a2[1] + 1)):
                if a1[v1] != a1[v2]:
                    return a1[v1] < a1[v2]
            return False
        v1 = []
        v2 = v3 = 0
        for v4 in range(len(a1)):
            v3 += a1[v4] == '1'
            while v3 == a2 + 1:
                v3 -= a1[v2] == '1'
                v2 += 1
            while v2 < len(a1) and a1[v2] == '0':
                v2 += 1
            if v3 == a2:
                if not v1 or check([v2, v4], v1):
                    v1 = [v2, v4]
        return a1[v1[0]:v1[1] + 1] if v1 else ''
