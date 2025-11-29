class C1(object):

    def maxNumOfSubstrings(self, a1):
        """
        """

        def find_right_from_left(a1, a2, a3, a4):
            v1, v2 = (a3[ord(a1[a4]) - ord('a')], a4)
            while v2 <= v1:
                if a2[ord(a1[v2]) - ord('a')] < a4:
                    return -1
                v1 = max(v1, a3[ord(a1[v2]) - ord('a')])
                v2 += 1
            return v1
        v1, v2 = ([float('inf')] * 26, [float('-inf')] * 26)
        for v3, v4 in enumerate(a1):
            v1[ord(v4) - ord('a')] = min(v1[ord(v4) - ord('a')], v3)
            v2[ord(v4) - ord('a')] = max(v2[ord(v4) - ord('a')], v3)
        v5 = []
        for v4 in range(len(v1)):
            if v1[v4] == float('inf'):
                continue
            v6, v7 = (v1[v4], find_right_from_left(a1, v1, v2, v1[v4]))
            if v7 != -1:
                v5.append((v7, v6))
        v5.sort()
        v8, v9 = ([], -1)
        for v7, v6 in v5:
            if v6 <= v9:
                continue
            v8.append(a1[v6:v7 + 1])
            v9 = v7
        return v8
