import collections

class C1(object):

    def longestDupSubstring(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return ''
        v2 = 1000000009
        v3 = 29
        v4 = [1] * (v1 + 1)
        for v5 in range(1, v1 + 1):
            v4[v5] = v4[v5 - 1] * v3 % v2
        v6 = [0] * (v1 + 1)
        for v5 in range(v1):
            v6[v5 + 1] = (v6[v5] * v3 + ord(a1[v5]) - ord('a')) % v2

        def find_pos(a1):
            v1 = collections.defaultdict(list)
            for v2 in range(v1 - a1 + 1):
                v3 = (v6[v2 + a1] - v6[v2] * v4[a1] % v2 + v2) % v2
                for v4 in v1[v3]:
                    if a1[v4:v4 + a1] == a1[v2:v2 + a1]:
                        return v4
                v1[v3].append(v2)
            return -1
        v7 = 1
        v8 = v1 - 1
        while v7 <= v8:
            v9 = v7 + (v8 - v7) // 2
            if find_pos(v9) != -1:
                v7 = v9 + 1
            else:
                v8 = v9 - 1
        v10 = v8
        v11 = find_pos(v10)
        return a1[v11:v11 + v10]
