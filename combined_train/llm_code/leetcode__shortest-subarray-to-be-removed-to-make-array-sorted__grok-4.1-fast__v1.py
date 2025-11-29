class C1:

    def findLengthOfShortestSubarray(self, a1: list[int]) -> int:
        v1 = len(a1)
        if v1 <= 1:
            return 0
        v2 = v1
        for v3 in range(v1 - 2, -1, -1):
            if a1[v3] > a1[v3 + 1]:
                v2 = v3 + 1
                break
        if v2 == 0:
            return 0
        v4 = v2
        for v5 in range(1, v2):
            if a1[v5] < a1[v5 - 1]:
                v4 = v5 - 1
                break
        v6 = v2
        v7 = v2
        for v8 in range(v4 + 1):
            while v7 < v1 and a1[v8] > a1[v7]:
                v7 += 1
            v6 = min(v6, v7 - v8 - 1)
        return v6
