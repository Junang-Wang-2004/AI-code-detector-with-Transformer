import collections


class Fenwick(object):
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


class Solution(object):
    def minInteger(self, num, k):
        n = len(num)
        ft = Fenwick(n)
        for i in range(1, n + 1):
            ft.update(i, 1)
        digs_pos = [collections.deque() for _ in range(10)]
        for i in range(n):
            d = int(num[i])
            digs_pos[d].append(i + 1)
        ans = []
        for _ in range(n):
            for d in range(10):
                if digs_pos[d]:
                    pos = digs_pos[d][0]
                    skips = ft.prefix_sum(pos - 1)
                    if skips <= k:
                        k -= skips
                        ft.update(pos, -1)
                        digs_pos[d].popleft()
                        ans.append(str(d))
                        break
        return "".join(ans)
