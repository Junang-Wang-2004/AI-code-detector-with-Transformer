class Solution:
    def lexicographicallySmallestString(self, s):
        n = len(s)
        can_remove = [[False] * n for _ in range(n)]
        diffs = {1, 25}
        for p in range(n - 1):
            if abs(ord(s[p]) - ord(s[p + 1])) in diffs:
                can_remove[p][p + 1] = True
        for sz in range(4, n + 1, 2):
            for begin in range(n - sz + 1):
                finish = begin + sz - 1
                if (abs(ord(s[begin]) - ord(s[finish])) in diffs and
                    can_remove[begin + 1][finish - 1]):
                    can_remove[begin][finish] = True
                for div in range(begin + 1, finish, 2):
                    if can_remove[begin][div] and can_remove[div + 1][finish]:
                        can_remove[begin][finish] = True
                        break
        remain = [""] * (n + 1)
        for pos in range(n - 1, -1, -1):
            option = s[pos] + remain[pos + 1]
            nxt = pos + 1
            while nxt < n:
                if can_remove[pos][nxt]:
                    option = min(option, remain[nxt + 1])
                nxt += 2
            remain[pos] = option
        return remain[0]
