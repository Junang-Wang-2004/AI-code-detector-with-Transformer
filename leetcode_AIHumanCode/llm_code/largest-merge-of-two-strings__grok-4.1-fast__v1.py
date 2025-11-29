class Solution(object):
    def largestMerge(self, word1, word2):
        ans = []
        i, j = 0, 0
        N, M = len(word1), len(word2)
        while i < N or j < M:
            x, y = i, j
            while x < N and y < M and word1[x] == word2[y]:
                x += 1
                y += 1
            if x < N and (y == M or word1[x] > word2[y]):
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        return "".join(ans)
