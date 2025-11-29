class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        m, n = len(str1), len(str2)
        prev = [[0] * (n + 1) for _ in range(m + 1)]
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                if str1[x - 1] == str2[y - 1]:
                    prev[x][y] = prev[x - 1][y - 1] + 1
                else:
                    prev[x][y] = max(prev[x - 1][y], prev[x][y - 1])
        ans = []
        p, q = m, n
        while p or q:
            if p and q and str1[p - 1] == str2[q - 1]:
                ans.append(str1[p - 1])
                p -= 1
                q -= 1
            elif p and (not q or prev[p][q] == prev[p - 1][q]):
                ans.append(str1[p - 1])
                p -= 1
            else:
                ans.append(str2[q - 1])
                q -= 1
        return ''.join(ans[::-1])
