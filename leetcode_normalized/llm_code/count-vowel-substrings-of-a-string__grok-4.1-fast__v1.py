class C1:

    def countVowelSubstrings(self, a1):
        v1 = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def subs_with_at_most(a1):
            v1 = [0] * 5
            v2 = 0
            v3 = 0
            v4 = 0
            for v5 in range(len(a1)):
                if a1[v5] not in v1:
                    v1 = [0] * 5
                    v2 = 0
                    v3 = v5 + 1
                    continue
                v6 = v1[a1[v5]]
                if v1[v6] == 0:
                    v2 += 1
                v1[v6] += 1
                while v2 > a1 and v3 <= v5:
                    v7 = v1[a1[v3]]
                    v1[v7] -= 1
                    if v1[v7] == 0:
                        v2 -= 1
                    v3 += 1
                v4 += v5 - v3 + 1
            return v4
        return subs_with_at_most(5) - subs_with_at_most(4)
