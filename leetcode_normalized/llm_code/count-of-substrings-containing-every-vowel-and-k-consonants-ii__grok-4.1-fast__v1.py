class C1:

    def countOfSubstrings(self, a1, a2):

        def num_with_all_vowels_ge_cons(a1):
            v1 = len(a1)
            v2 = [0] * 26
            v3 = 0
            v4 = 0
            v5 = 0
            v6 = 0
            v7 = set('aeiou')
            for v8 in range(v1):
                v9 = ord(a1[v8]) - ord('a')
                if a1[v8] in v7:
                    if v2[v9] == 0:
                        v3 += 1
                    v2[v9] += 1
                else:
                    v4 += 1
                while v3 == 5 and v4 >= a1:
                    v5 += v1 - v8
                    v10 = ord(a1[v6]) - ord('a')
                    if a1[v6] in v7:
                        v2[v10] -= 1
                        if v2[v10] == 0:
                            v3 -= 1
                    else:
                        v4 -= 1
                    v6 += 1
            return v5
        return num_with_all_vowels_ge_cons(a2) - num_with_all_vowels_ge_cons(a2 + 1)
