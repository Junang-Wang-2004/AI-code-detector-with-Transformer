class Solution:
    def getWordsInLongestSubsequence(self, n, words, groups):
        lengths = [1] * n
        next_pos = [-1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    diff_cnt = 0
                    for a, b in zip(words[i], words[j]):
                        if a != b:
                            diff_cnt += 1
                            if diff_cnt > 1:
                                break
                    if diff_cnt == 1 and lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        next_pos[i] = j
        start_idx = 0
        for k in range(1, n):
            if lengths[k] > lengths[start_idx]:
                start_idx = k
        res = []
        pos = start_idx
        while pos != -1:
            res.append(words[pos])
            pos = next_pos[pos]
        return res
