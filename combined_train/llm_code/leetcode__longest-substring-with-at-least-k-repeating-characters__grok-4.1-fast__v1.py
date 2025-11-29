class C1:

    def longestSubstring(self, a1, a2):
        v1 = 0
        v2 = [(0, len(a1))]
        while v2:
            v3, v4 = v2.pop()
            if v4 - v3 <= v1:
                continue
            v5 = [0] * 26
            for v6 in range(v3, v4):
                v5[ord(a1[v6]) - ord('a')] += 1
            v6 = v3
            while v6 < v4:
                while v6 < v4 and v5[ord(a1[v6]) - ord('a')] < a2:
                    v6 += 1
                if v6 == v4:
                    break
                v7 = v6
                while v7 < v4 and v5[ord(a1[v7]) - ord('a')] >= a2:
                    v7 += 1
                v8 = v7 - v6
                if v6 == v3 and v7 == v4:
                    v1 = max(v1, v8)
                else:
                    v2.append((v6, v7))
                v6 = v7
        return v1
