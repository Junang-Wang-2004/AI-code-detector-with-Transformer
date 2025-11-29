from functools import reduce

class C1(object):

    def numberOfCombinations(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def find_longest_common_prefix(a1):
            v1 = [[0] * (len(a1) + 1) for v2 in range(len(a1) + 1)]
            for v3 in reversed(range(len(v1) - 1)):
                for v4 in reversed(range(len(v1[0]) - 1)):
                    if a1[v3] == a1[v4]:
                        v1[v3][v4] = v1[v3 + 1][v4 + 1] + 1
            return v1

        def is_less_or_equal_to_with_same_length(a1, a2, a3, a4, a5):
            return a2[a3][a4] >= a5 or a1[a3 + a2[a3][a4]] < a1[a4 + a2[a3][a4]]
        v2 = find_longest_common_prefix(a1)
        v3 = [[0] * len(a1) for v4 in range(len(a1))]
        v3[0][0] = int(a1[0] != '0')
        for v5 in range(1, len(a1)):
            v3[v5][v5] = v3[v5 - 1][v5 - 1]
            if a1[v5] == '0':
                continue
            v6 = 0
            for v7 in range(len(a1) - v5 + 1):
                v8 = v5 + v7 - 1
                v3[v8][v7 - 1] = v6
                if v5 - v7 < 0:
                    continue
                if a1[v5 - v7] != '0' and is_less_or_equal_to_with_same_length(a1, v2, v5 - v7, v5, v7):
                    v3[v8][v7 - 1] = (v3[v8][v7 - 1] + v3[v5 - 1][v7 - 1]) % v1
                v6 = (v6 + v3[v5 - 1][v7 - 1]) % v1
        return reduce(lambda total, x: (total + x) % v1, v3[-1], 0)
