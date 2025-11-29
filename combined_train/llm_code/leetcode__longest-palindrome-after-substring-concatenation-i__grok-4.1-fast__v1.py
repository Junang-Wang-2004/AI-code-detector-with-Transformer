class C1:

    def longestPalindrome(self, a1, a2):
        v1 = a2[::-1]

        def pal_prefix_lens(a1):
            v1 = len(a1)
            v2 = [1] * v1
            for v3 in range(v1):
                v4, v5 = (v3, v3)
                while v4 >= 0 and v5 < v1 and (a1[v4] == a1[v5]):
                    v2[v4] = max(v2[v4], v5 - v4 + 1)
                    v4 -= 1
                    v5 += 1
                v4, v5 = (v3, v3 + 1)
                while v4 >= 0 and v5 < v1 and (a1[v4] == a1[v5]):
                    v2[v4] = max(v2[v4], v5 - v4 + 1)
                    v4 -= 1
                    v5 += 1
            return v2 + [0]
        v2 = pal_prefix_lens(a1)
        v3 = pal_prefix_lens(v1)
        v4, v5 = (len(a1), len(v1))
        v6 = 0
        v7 = [[0] * (v5 + 1) for v8 in range(2)]
        for v9 in range(v4):
            v10 = v9 % 2
            v11 = 1 - v10
            v7[v10][0] = 0
            for v12 in range(v5):
                v13 = a1[v9] == v1[v12]
                v7[v10][v12 + 1] = v7[v11][v12] + 2 if v13 else 0
                v14 = 1 if v13 else 0
                v6 = max(v6, v7[v10][v12 + 1] + v2[v9 + v14])
                v6 = max(v6, v7[v10][v12 + 1] + v3[v12 + v14])
        return v6
