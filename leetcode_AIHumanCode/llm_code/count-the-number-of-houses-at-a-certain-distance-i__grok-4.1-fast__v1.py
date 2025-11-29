class Solution:
    def countOfPairs(self, n, x, y):
        x -= 1
        y -= 1
        res = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                direct = abs(i - j)
                via1 = abs(i - x) + 1 + abs(j - y)
                via2 = abs(i - y) + 1 + abs(j - x)
                d = min(direct, via1, via2)
                res[d - 1] += 1
        return res
