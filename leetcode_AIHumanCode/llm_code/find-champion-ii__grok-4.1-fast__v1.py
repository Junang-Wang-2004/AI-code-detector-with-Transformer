class Solution:
    def findChampion(self, n, edges):
        targets = set()
        for _, v in edges:
            targets.add(v)
        if len(targets) != n - 1:
            return -1
        total = n * (n - 1) // 2
        tsum = sum(targets)
        return total - tsum
