v1 = [1]
v2 = {1: 0}
for v3 in range(1, 26):
    v1.append(v1[-1] << 1)
    v2[v1[v3]] = v3

class C1(object):

    def maxLength(self, a1):
        """
        """

        def bitset(a1):
            v1 = 0
            for v2 in a1:
                if v1 & v1[ord(v2) - ord('a')]:
                    return 0
                v1 |= v1[ord(v2) - ord('a')]
            return v1

        def number_of_one(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1 = [0]
        for v2 in a1:
            v3 = bitset(v2)
            if not v3:
                continue
            v4 = len(v1)
            for v5 in range(v4):
                if v1[v5] & v3:
                    continue
                v1.append(v1[v5] | v3)
        return max((number_of_one(s_set) for v6 in v1))
