class Solution:
    def strangePrinter(self, s):
        size = len(s)
        if not size:
            return 0
        costs = [[0] * size for _ in range(size)]
        for idx in range(size):
            costs[idx][idx] = 1
        for span in range(2, size + 1):
            for begin in range(size - span + 1):
                finish = begin + span - 1
                costs[begin][finish] = costs[begin][finish - 1] + 1
                for pos in range(begin, finish):
                    if s[pos] == s[finish]:
                        extra = costs[pos + 1][finish - 1] if pos + 1 <= finish - 1 else 0
                        costs[begin][finish] = min(costs[begin][finish], costs[begin][pos] + extra)
        return costs[0][size - 1]
