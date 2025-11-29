class C1(object):

    def countOfSubstrings(self, a1, a2):
        v1 = set('aeiou')
        v2 = 5

        def at_least(a1):
            v1 = len(a1)
            v2 = [0] * 26
            v3 = 0
            v4 = 0
            v5 = 0
            v6 = 0
            for v7 in range(v1):
                v8 = ord(a1[v7]) - ord('a')
                if a1[v7] in v1:
                    if v2[v8] == 0:
                        v4 += 1
                    v2[v8] += 1
                else:
                    v3 += 1
                while v4 == v2 and v3 >= a1:
                    v5 += v1 - v7
                    v9 = ord(a1[v6]) - ord('a')
                    if a1[v6] in v1:
                        v2[v9] -= 1
                        if v2[v9] == 0:
                            v4 -= 1
                    else:
                        v3 -= 1
                    v6 += 1
            return v5
        return at_least(a2) - at_least(a2 + 1)
