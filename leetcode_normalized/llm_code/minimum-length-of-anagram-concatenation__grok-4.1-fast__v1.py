class C1(object):

    def minAnagramLength(self, a1):
        v1 = len(a1)
        v2 = []
        v3 = int(v1 ** 0.5) + 1
        for v4 in range(1, v3):
            if v1 % v4 == 0:
                v2.append(v4)
                v5 = v1 // v4
                if v4 != v5:
                    v2.append(v5)
        v2.sort()

        def char_counts(a1, a2):
            v1 = [0] * 26
            for v2 in range(a1, a1 + a2):
                v1[ord(a1[v2]) - ord('a')] += 1
            return v1

        def segments_match(a1):
            v1 = char_counts(0, a1)
            v2 = a1
            while v2 < v1:
                if char_counts(v2, a1) != v1:
                    return False
                v2 += a1
            return True
        for v6 in v2:
            if segments_match(v6):
                return v6
