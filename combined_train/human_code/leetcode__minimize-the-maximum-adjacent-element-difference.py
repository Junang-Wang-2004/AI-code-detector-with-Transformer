class C1(object):

    def minDifference(self, a1):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                if a1[v3] == -1:
                    v2 += 1
                    continue
                if v1 and v2 and (min((max(abs(v1 - x), abs(a1[v3] - x)) for v4 in (left + a1, right - a1))) > a1) and (v2 == 1 or right - a1 - (left + a1) > a1):
                    return False
                v1 = a1[v3]
                v2 = 0
            return True
        v1, v2, v3 = (0, float('inf'), 0)
        for v4 in range(len(a1)):
            if a1[v4] != -1:
                if v4 + 1 < len(a1) and a1[v4 + 1] != -1:
                    v1 = max(v1, abs(a1[v4] - a1[v4 + 1]))
                continue
            if v4 - 1 < len(a1) and a1[v4 - 1] != -1:
                v2 = min(v2, a1[v4 - 1])
                v3 = max(v3, a1[v4 - 1])
            if v4 + 1 < len(a1) and a1[v4 + 1] != -1:
                v2 = min(v2, a1[v4 + 1])
                v3 = max(v3, a1[v4 + 1])
        return binary_search(v1, (v3 - v2) // 2, check)
