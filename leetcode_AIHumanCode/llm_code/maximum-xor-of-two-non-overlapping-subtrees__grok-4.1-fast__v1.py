class TrieNode:
    def __init__(self):
        self.children = [None] * 2

class XorTrie:
    def __init__(self, bits):
        self.root = TrieNode()
        self.bits = bits

    def insert(self, val):
        curr = self.root
        for k in range(self.bits - 1, -1, -1):
            b = (val >> k) & 1
            if not curr.children[b]:
                curr.children[b] = TrieNode()
            curr = curr.children[b]

    def get_max_xor(self, val):
        if not self.root.children[0] and not self.root.children[1]:
            return 0
        curr = self.root
        mx = 0
        for k in range(self.bits - 1, -1, -1):
            b = (val >> k) & 1
            opp = 1 - b
            if curr.children[opp]:
                mx |= (1 << k)
                curr = curr.children[opp]
            else:
                curr = curr.children[b]
        return mx

class Solution:
    def maxXor(self, n, edges, values):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        subtree = [0] * n

        def calc(node, par):
            tot = values[node]
            for nxt in graph[node]:
                if nxt != par:
                    tot += calc(nxt, node)
            subtree[node] = tot
            return tot

        calc(0, -1)

        if n == 1:
            return 0

        bl = max(subtree).bit_length()

        tr = XorTrie(bl)

        def search(node, par):
            res = tr.get_max_xor(subtree[node])
            for nxt in graph[node]:
                if nxt != par:
                    res = max(res, search(nxt, node))
            tr.insert(subtree[node])
            return res

        return search(0, -1)
