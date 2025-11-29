class Solution(object):
    def gcdSort(self, nums):
        n = len(nums)
        if n == 0:
            return True
        mx = max(nums)
        parent = list(range(mx + 1))
        rank = [0] * (mx + 1)

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            cur = x
            while cur != root:
                nxt = parent[cur]
                parent[cur] = root
                cur = nxt
            return root

        def unite(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        spf = list(range(mx + 1))
        sq = int(mx ** 0.5) + 1
        for i in range(2, sq):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        unique_nums = set(nums)
        for num in unique_nums:
            if num < 2:
                continue
            x = num
            while x > 1:
                p = spf[x]
                unite(num - 1, p - 1)
                while x % p == 0:
                    x //= p

        snums = sorted(nums)
        for i in range(n):
            if find(nums[i] - 1) != find(snums[i] - 1):
                return False
        return True
