# Time:  O(nlogn)
# Space: O(n)

import collections


class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = list(map(self.find_set, (x, y)))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        return True


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        """
        union_find = UnionFind(len(s))
        for x,y in pairs: 
            union_find.union_set(x, y)
        components = collections.defaultdict(list)
        for i in range(len(s)): 
            components[union_find.find_set(i)].append(s[i])
        for i in components.keys(): 
            components[i].sort(reverse=True)
        result = []
        for i in range(len(s)): 
            result.append(components[union_find.find_set(i)].pop())
        return "".join(result)


