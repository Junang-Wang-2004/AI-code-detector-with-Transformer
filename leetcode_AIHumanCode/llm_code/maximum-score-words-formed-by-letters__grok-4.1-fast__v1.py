class Solution:
    def maxScoreWords(self, words, letters, score):
        n = len(words)
        reqs = [[0] * 26 for _ in range(n)]
        pts = [0] * n
        for i in range(n):
            for ch in words[i]:
                j = ord(ch) - ord('a')
                reqs[i][j] += 1
                pts[i] += score[j]
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - ord('a')] += 1
        self.ans = 0
        def search(i, val, cnt):
            self.ans = max(self.ans, val)
            if i == n:
                return
            search(i + 1, val, cnt)
            need = reqs[i]
            if all(cnt[k] >= need[k] for k in range(26)):
                for k in range(26):
                    cnt[k] -= need[k]
                search(i + 1, val + pts[i], cnt)
                for k in range(26):
                    cnt[k] += need[k]
        search(0, 0, avail)
        return self.ans
