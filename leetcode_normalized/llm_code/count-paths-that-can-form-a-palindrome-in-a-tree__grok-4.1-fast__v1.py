from collections import deque, defaultdict

class C1:

    def countPalindromePaths(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(1, v1):
            v5 = a1[v4]
            if v5 != -1:
                v2[v5].append(v4)
        v6 = defaultdict(int)
        v6[0] = 1
        v7 = 0
        v8 = deque([(0, 0)])
        while v8:
            v9, v10 = v8.popleft()
            v11 = 1 << ord(a2[v9]) - ord('a')
            v12 = v10 ^ v11
            v7 += v6[v12]
            for v13 in range(26):
                v7 += v6[v12 ^ 1 << v13]
            v6[v12] += 1
            for v14 in v2[v9]:
                v8.append((v14, v12))
        return v7
